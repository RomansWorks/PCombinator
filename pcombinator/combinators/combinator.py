import json
from typing import Any, Dict, List, NewType, Type, Union
from pydantic import BaseModel, Field, model_validator, root_validator, validator

from pcombinator.util.classname import get_fully_qualified_class_name

IdTree = NewType("IdTree", Dict[str, "IdTree"])


class Combinator(BaseModel):
    """
    Base class for combinators.
    """

    combinator_type: str = Field(default=None, init=False)
    id: str

    def __init__(self, id, **kwargs):
        super().__init__(id=id, **kwargs)

        self.id = id
        if "combinator_type" in kwargs:
            # From deserialization
            self.combinator_type = kwargs["combinator_type"]
            # Verify that the combinator type is known
            self.__class__.verify_known_combinator_type(self.combinator_type)
        else:
            # Otherwise
            self.combinator_type = get_fully_qualified_class_name(self.__class__)
            # Allow implicit registration of derived classes
            self.__class__.register_derived_class(self.__class__)

    @classmethod
    def verify_known_combinator_type(cls, combinator_type: str):
        if combinator_type not in derived_classes:
            raise ValueError(
                f"No registered combinator implementation for: {combinator_type}"
            )

    @classmethod
    def register_derived_class(cls, derived_class: Type["Combinator"]):
        fq_cls_name = get_fully_qualified_class_name(derived_class)
        # Verify that this has not been registered before with a different name
        if fq_cls_name in derived_classes:
            if derived_classes[fq_cls_name] != derived_class:
                raise ValueError(
                    f"Class {fq_cls_name} already registered with a different class"
                )
        else:
            derived_classes[fq_cls_name] = derived_class

    def get_id(self):
        """
        Get the id of the combinator.
        """
        return self.id

    def render(self) -> tuple[Union[str, None], IdTree]:
        """
        Render self. To be implemented by subclasses.

        Note that it is expected that the output will contain the own id in the IdTree.
        """
        raise NotImplementedError("render() not implemented")

    def to_json(self):
        return self.model_dump_json()

    @model_validator(mode="before")
    def parse_nested(cls, values):
        print("parse_nested called", values)
        # If values is a dict, create an instance of the appropriate class
        if not isinstance(values, dict):
            return values
        else:
            # Walk the children tree and convert each to an object
            children = values.get("children")
            if children is None:
                return values

            # If children is a list, then convert all dicts in the list to objects
            if isinstance(children, list):
                for i, child in enumerate(children):
                    if isinstance(child, dict):
                        children[i] = combinator_dict_to_obj(children, i, child)
                return values

            # If children is a dict, then convert all values in the dict to objects and keep the keys
            if isinstance(children, dict):
                for key, child in children.items():
                    if isinstance(child, dict):
                        child = combinator_dict_to_obj(child)
                        children[key] = child
                return values

            # Otherwise we don't know how to handle this children list
            # TODO: It'd be better to move the conversion logic to the derived classes, since these know the structure of the children
            raise ValueError(f"parse_nested: cannot convert children: {children}")

    @classmethod
    def from_json(cls, json_str: str):
        print("from_json called", json_str)
        dict = json.loads(json_str)
        combinator_type = dict["combinator_type"]
        # dict.pop("combinator_type")  # Remove so that we don't confuse pydantic
        if combinator_type in derived_classes:
            return derived_classes[combinator_type].model_validate_strings(dict)
        else:
            raise ValueError(f"Unknown combinator type (from_json): {combinator_type}")
        # data = validate_json(json_str)
        # combinator_type = data["_combinator_type"]
        # if combinator_type in derived_classes:
        #     return derived_classes[combinator_type].from_json(data)
        # else:
        #     raise ValueError(f"Unknown combinator type: {combinator_type}")


def render_children(
    children: List[Union["Combinator", str, None]]
) -> tuple[List[Union[str, None]], IdTree]:
    """
    Recursively render children.
    For each rendered child, include the rendered child's id tree in the returned IdTree.

    Returns:
        rendered_children: A list of rendered children
        rendered_children_id_tree: An IdTree of rendered children
    """
    rendered_children = []
    rendered_children_id_tree = {}
    for child in children:
        if isinstance(child, str):
            rendered_children.append(child)
            # rendered_child_id_tree[child.__hash__()] = {}
            continue
        elif child is None:
            continue
        rendered_child, rendered_child_id_tree = child.render()
        rendered_children.append(rendered_child)
        rendered_children_id_tree.update(rendered_child_id_tree)
        # rendered_children_id_tree[child.get_id()] = rendered_child_id_tree

    return rendered_children, rendered_children_id_tree


# Map of combinator types to classes
derived_classes: Dict[str, Type[Combinator]] = {}


def combinator_dict_to_obj(child):
    combinator_type = child.get("combinator_type")
    if combinator_type is not None:
        if combinator_type in derived_classes:
            derived_class = derived_classes[combinator_type]
            return derived_class.model_validate_strings(child)
        else:
            raise ValueError(
                f"combinator_dict_to_obj: cannot convert dict to combinator object - unknown combinator type: {combinator_type}"
            )

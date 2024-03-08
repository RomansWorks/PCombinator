import inspect
import json
from typing import Any, Dict, List, NewType, Optional, Type, Union

from pcombinator.util.classname import get_fully_qualified_class_name

IdTree = NewType("IdTree", Dict[str, "IdTree"])


class Combinator:
    """
    Base class for combinators.
    """

    combinator_type: str
    id: str

    def __init__(self, id: str, combinator_type: Optional[str], **kwargs):
        super().__init__(**kwargs)

        self.id = id
        if combinator_type is not None:
            # From deserialization
            self.combinator_type = combinator_type
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
    def register_derived_class(cls, derived_class):
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

    # def __dict__(self):
    #     """
    #     Create a dict over public fields of the combinator and of any derived classes.
    #     """
    #     # First get the list of public fields (only variables, no functions)
    #     public_field_names = [name for name, value in self.__dict__.items()]

    #     public_fields = [name for name, value in public_field_names]

    #     # Return a dict
    #     return {field: getattr(self, field) for field in public_fields}

    # def __iter__(self):
    #     """
    #     Create an iterator over the public fields of the combinator and of any derived classes.
    #     """
    #     for field, value in self.__dict__.items():
    #         yield field, value

    @staticmethod
    def default(obj):
        """
        Default method to serialize objects. If the object has a `to_json` method, it uses it.
        """
        if hasattr(obj, "to_json"):
            return obj.to_json()
        raise TypeError(
            f"default() - Object of type {obj.__class__.__name__} is not JSON serializable"
        )

    def to_json(self):
        return json.dumps(
            self.to_dict(),
            default=self.default,
        )

    def to_dict(self):
        res = {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
        return res

    @classmethod
    def from_dict(cls, values: dict):
        """
        Create a new combinator from a dictionary.
        """
        combinator_type = values["combinator_type"]
        if combinator_type in derived_classes:
            return derived_classes[combinator_type].from_json(values)
        else:
            raise ValueError(f"Unknown combinator type (from_json): {combinator_type}")

    @classmethod
    def from_json(cls, json_str: str):
        if not json_str.startswith("{"):
            # Workaround for the stange nesting rules of the json parser
            return json_str
        values = json.loads(json_str)
        # If string value or none just return the value
        if not isinstance(values, dict):
            return values
        return cls.from_dict(values)


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


def combinator_dict_to_obj(
    child: Union[dict, str, None]
) -> Union[str, None, Combinator]:
    # No need to convert string and None
    if not isinstance(child, dict):
        return child

    combinator_type = child.get("combinator_type")
    if combinator_type in derived_classes:
        derived_class = derived_classes[combinator_type]
        return derived_class(child)  # TODO: need to unwrap the dict
    else:
        raise ValueError(
            f"combinator_dict_to_obj: cannot convert dict to combinator object - unknown combinator type: {combinator_type}"
        )

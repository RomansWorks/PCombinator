import json
from typing import Dict
from jinja2 import Template

from pcombinator.combinators.combinator import (
    Combinator,
    IdTree,
    combinator_dict_to_obj,
    render_children,
    derived_classes,
)
from pcombinator.combinators.combinator_or_leaf_type import CombinatorOrLeaf
from pcombinator.util.classname import get_fully_qualified_class_name


class Jinja2TemplateCombinator(Combinator):
    """
    A combinator that renders a template with its rendered children as arguments.
    """

    # _combinator_type: Literal["jinja2_template"] = "jinja2_template"

    _template: Template
    template_source: str
    children: Dict[str, CombinatorOrLeaf]

    def __init__(
        self,
        id: str,
        template_source: str,
        children: Dict[str, CombinatorOrLeaf],
        **kwargs,
    ):
        super().__init__(
            id=id,
            combinator_type=kwargs.get("combinator_type")
            or get_fully_qualified_class_name(self.__class__),
        )
        self._template = Template(source=template_source)
        self.template_source = template_source
        self.children = children

    def render(self) -> tuple[str, IdTree]:
        """
        Render the template, passing the rendered children as arguments.

        Returns:
            rendered: The rendered template
            rendered_id_tree: An IdTree of rendered children under this combinator id.
        """
        rendered_children_dict = {}
        res_id_tree = {self.id: {}}
        for key in self.children.keys():
            rendered, id_tree = render_children([self.children[key]])
            res_id_tree[self.id][key] = id_tree
            rendered_children_dict[key] = rendered[0]

        res = self._template.render(rendered_children_dict)
        return res, res_id_tree

    def add_child(self, key: str, child: CombinatorOrLeaf) -> None:
        self.children[key] = child

    def get_children(self) -> Dict[str, CombinatorOrLeaf]:
        return self.children

    def remove_child_by_key(self, key: str) -> None:
        del self.children[key]

    def remove_child_by_id(self, id: str) -> None:
        for key, child in self.children.items():
            if child.get_id() == id:
                del self.children[key]
                return

    # def to_json(self):
    #     return json.dumps(
    #         {k: v for k, v in self.__dict__.items() if not k.startswith("_")}
    #     )

    @classmethod
    def from_json(cls, values: dict):

        return cls(
            id=values["id"],
            template_source=values["template_source"],
            children={
                key: Combinator.from_json(child) if child.startswith("{") else child
                for key, child in values["children"].items()
            },
        )

        # # Walk the children tree and convert each to an object
        # children = values.get("children")
        # # # If children is a list, then convert all dicts in the list to objects
        # # if isinstance(children, list):
        # #     for i, child in enumerate(children):
        # #         if isinstance(child, dict):
        # #             children[i] = combinator_dict_to_obj(children, i, child)
        # #     return values

        # # If children is a dict, then convert all values in the dict to objects and keep the keys
        # if isinstance(children, dict):
        #     for key, child in children.items():
        #         if isinstance(child, dict):
        #             child = combinator_dict_to_obj(child)
        #             children[key] = child
        #     values["children"] = children

        # # return Jinja2TemplateCombinator(**values)
        # return cls(**values)


Combinator.register_derived_class(Jinja2TemplateCombinator)

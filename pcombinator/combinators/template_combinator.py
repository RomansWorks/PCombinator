from typing import Dict
from jinja2 import Template
from pydantic import PrivateAttr

from pcombinator.combinators.combinator import (
    Combinator,
    IdTree,
    render_children,
    derived_classes,
)
from pcombinator.combinators.combinator_or_leaf_type import CombinatorOrLeaf


class Jinja2TemplateCombinator(Combinator):
    """
    A combinator that renders a template with its rendered children as arguments.
    """

    # _combinator_type: Literal["jinja2_template"] = "jinja2_template"

    _template: Template = PrivateAttr()
    template_source: str
    children: Dict[str, CombinatorOrLeaf]

    def __init__(
        self,
        id: str,
        template_source: str,
        children: Dict[str, CombinatorOrLeaf],
    ):
        super().__init__(
            id=id,
            template_source=template_source,
            children=children,
            # _combinator_type=self._combinator_type,
            # combinator_type=__class__.__name__,
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
    #     return {
    #         "combinator_type": self._combinator_type,
    #         "id": self.id,
    #         "template_source": self.template_source,
    #         "children": {
    #             key: self._child_to_json(child) for key, child in self.children.items()
    #         },
    #     }

    # def _child_to_json(self, child: CombinatorOrLeaf):
    #     if isinstance(child, str):
    #         return child
    #     elif child is None:
    #         return None
    #     else:
    #         return child.to_json()


# derived_classes["jinja2_template"] = Jinja2TemplateCombinator
# derived_classes[Jinja2TemplateCombinator.__name__] = Jinja2TemplateCombinator

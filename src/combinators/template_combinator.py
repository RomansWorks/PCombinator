from typing import Dict
from jinja2 import Template

from src.combinators.combinator import Combinator, IdTree


class TemplateCombinator(Combinator):
    children: Dict[str, "Combinator"]

    def __init__(self, template: Template, children: Dict[str, "Combinator"], id=None):
        super().__init__(id)
        self.template = template
        self.children = children

    def render(self) -> (str, IdTree):
        # Get an ordered list of keys to match render results
        keys = self.children.keys()
        children_as_list = [self.children[k] for k in keys]
        rendered_children, rendered_child_id_tree = super().render_children(
            children_as_list
        )
        rendered_children_dict = dict(zip(keys, rendered_children))
        res = self.template.render(rendered_children_dict)

        return res, {self.id: rendered_child_id_tree}

    def add_child(self, key: str, child: "Combinator") -> None:
        self.children[key] = child

    def get_children(self) -> Dict[str, "Combinator"]:
        return self.children

    def remove_child_by_key(self, key: str) -> None:
        del self.children[key]

    def remove_child_by_id(self, id: str) -> None:
        for key, child in self.children.items():
            if child.get_id() == id:
                del self.children[key]
                return

from typing import Dict, List, NewType


IdTree = NewType("IdTree", Dict[str, "IdTree"])


class Combinator:
    _combinator_type: str

    def __init__(self, id=None):
        self.id = id

    def get_id(self):
        return self.id

    def render(self) -> (str, IdTree):
        raise NotImplementedError("render() not implemented")

    def render_children(children: List["Combinator"]) -> (List[str], IdTree):
        # Render all children
        rendered_children = []
        rendered_children_id_tree = {}
        for child in children:
            if isinstance(child, str):
                rendered_children.append(child)
                # rendered_child_id_tree[child.__hash__()] = {}
                continue
            rendered_child, rendered_child_id_tree = child.render()
            rendered_children.append(rendered_child)
            rendered_children_id_tree[child.get_id()] = rendered_child_id_tree

        return rendered_children, rendered_child_id_tree

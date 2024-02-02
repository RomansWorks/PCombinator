from typing import Dict, List, NewType, Union
from pydantic import BaseModel

IdTree = NewType("IdTree", Dict[str, "IdTree"])


class Combinator(BaseModel):
    """
    Base class for combinators.
    """

    _combinator_type: str
    _id: str

    def __init__(self, id):
        super().__init__()
        self._id = id

    def get_id(self):
        """
        Get the id of the combinator.
        """
        return self._id

    def render(self) -> (Union[str, None], IdTree):
        """
        Render self. To be implemented by subclasses.

        Note that it is expected that the output will contain the own id in the IdTree.
        """
        raise NotImplementedError("render() not implemented")


def render_children(
    children: List[Union["Combinator", str, None]]
) -> (List[Union[str, None]], IdTree):
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

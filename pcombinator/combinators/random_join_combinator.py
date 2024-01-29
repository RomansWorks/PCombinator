import random
from typing import List, Literal, Union

from pcombinator.combinators.combinator import Combinator, IdTree, render_children


class RandomJoinCombinator(Combinator):
    """
    On render, this combinator will randomly select a number of children between n_min and n_max (inclusive)
    and join them with the separator.
    """

    _combinator_type: Literal["random_join"] = "random_join"

    children: List[Union["Combinator", str, None]]

    def __init__(
        self,
        n_min: int = 1,
        n_max: int = 1,
        separators: List[str] = ["\n"],
        seed: Union[int, None] = None,
        children: List[Union["Combinator", str, None]] = [],
        id: str = None,
    ):
        super().__init__(id=id)
        self.n_min = n_min
        self.n_max = n_max
        self.separators = separators
        self.random = random.Random(x=seed)
        self.children = children

    def render(self) -> (Union[str, None], IdTree):
        # Choose how many children will be selected
        n_children = self.random.randint(self.n_min, self.n_max)

        # Select children (without replacement)
        selected_children = self.random.sample(self.children, n_children)

        # Render children
        rendered_children, rendered_child_id_tree = render_children(selected_children)

        # Select separator
        separator = self.random.choice(self.separators)

        # Join children
        rendered = separator.join(rendered_children)

        # Return
        return rendered, {self.id: rendered_child_id_tree}

    def add_child(self, child: Union[Combinator, str, None]) -> None:
        self.children.append(child)

    def get_children(self) -> List[Union[Combinator, str]]:
        return self.children

    def remove_child_by_id(self, id: str) -> None:
        for i, child in enumerate(self.children):
            if child.get_id() == id:
                del self.children[i]
                return

    # def to_json(self):
    #     return {
    #         "combinator_type": self._combinator_type,
    #         "id": self.id,
    #         "n_min": self.n_min,
    #         "n_max": self.n_max,
    #         "separators": self.separators,
    #         "children": [self._child_to_json(child) for child in self.children],
    #     }

    # def _child_to_json(self, child: Union[Combinator, str, None]):
    #     if isinstance(child, str):
    #         return child
    #     elif child is None:
    #         return None
    #     else:
    #         return child.to_json()
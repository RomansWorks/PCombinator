import random as rnd
from typing import Any, List, Union

from pcombinator.combinators.combinator import (
    Combinator,
    IdTree,
    combinator_dict_to_obj,
    render_children,
    derived_classes,
)
from pcombinator.combinators.combinator_or_leaf_type import CombinatorOrLeaf
from pcombinator.util.classname import get_fully_qualified_class_name


class RandomJoinCombinator(Combinator):
    """
    On render, this combinator will randomly select a number of children between n_min and n_max (inclusive)
    and join them with the separator.
    """

    # _combinator_type: Literal["random_join"] = "random_join"

    children: List[CombinatorOrLeaf]
    n_min: int
    n_max: int
    separators: List[str]
    seed: Union[int, None]

    _random: Any

    def __init__(
        self,
        id: str,
        n_min: int = 1,
        n_max: int = 1,
        separators: List[str] = ["\n"],
        children: List[CombinatorOrLeaf] = [],
        seed: Union[int, None] = None,
        _random: Union[Any, None] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            combinator_type=kwargs.get("combinator_type")
            or get_fully_qualified_class_name(self.__class__),
        )
        self.n_min = n_min
        self.n_max = n_max
        self.separators = separators
        self._random = _random or rnd.Random(x=seed)
        self.seed = seed
        self.children = children

    def render(self) -> tuple[Union[str, None], IdTree]:
        # Choose how many children will be selected
        n_children = self._random.randint(self.n_min, self.n_max)

        # Select children (without replacement)
        selected_children = self._random.sample(self.children, n_children)

        # Render children
        rendered_children, rendered_child_id_tree = render_children(selected_children)

        # Select separator
        separator = self._random.choice(self.separators)

        # Join children
        rendered = separator.join(rendered_children)

        # Return
        return rendered, {self.id: rendered_child_id_tree}

    def add_child(self, child: CombinatorOrLeaf) -> None:
        self.children.append(child)

    def get_children(self) -> List[CombinatorOrLeaf]:
        return self.children

    def remove_child_by_id(self, id: str) -> None:
        for i, child in enumerate(self.children):
            if child.get_id() == id:
                del self.children[i]
                return

    @classmethod
    def from_json(cls, values: dict):

        return cls(
            id=values["id"],
            n_min=values["n_min"],
            n_max=values["n_max"],
            separators=values["separators"],
            children=[Combinator.from_json(child) for child in values["children"]],
            seed=values["seed"],
        )


Combinator.register_derived_class(RandomJoinCombinator)

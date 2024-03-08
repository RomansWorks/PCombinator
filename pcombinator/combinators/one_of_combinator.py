import random
from typing import List, Literal, Union
from pcombinator.combinators.combinator import Combinator, derived_classes
from pcombinator.combinators.combinator_or_leaf_type import CombinatorOrLeaf
from pcombinator.combinators.random_join_combinator import RandomJoinCombinator
from pcombinator.util.classname import get_fully_qualified_class_name


class OneOfCombinator(RandomJoinCombinator):
    """
    On render, this combinator will randomly select one of the children and render it.
    """

    children: List[CombinatorOrLeaf]
    # n_max: int
    # n_min: int
    # separators: List[str]
    # seed: Union[int, None]
    # random: random.Random

    def __init__(
        self,
        id: str,
        children: List[CombinatorOrLeaf] = [],
        seed: Union[int, None] = None,
        **kwargs,
    ):
        super().__init__(
            id=id,
            n_min=1,
            n_max=1,
            separators=[""],
            children=children,
            seed=seed,
            _random=random.Random(x=seed),
            combinator_type=kwargs.get("combinator_type")
            or get_fully_qualified_class_name(self.__class__),
        )

    @classmethod
    def from_json(cls, values: dict):
        return cls(
            id=values["id"],
            children=[Combinator.from_dict(child) for child in values["children"]],
            seed=values["seed"],
        )


Combinator.register_derived_class(OneOfCombinator)

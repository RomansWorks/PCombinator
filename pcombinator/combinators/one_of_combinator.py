from typing import List, Literal, Union
from pcombinator.combinators.combinator import Combinator
from pcombinator.combinators.random_join_combinator import RandomJoinCombinator


class OneOfCombinator(RandomJoinCombinator):
    """
    On render, this combinator will randomly select one of the children and render it.
    """

    _combinator_type: Literal["one_of"] = "one_of"

    def __init__(
        self,
        id: str,
        children: List[Union[Combinator, str, None]] = [],
        seed: Union[int, None] = None,
    ):
        super().__init__(
            id=id, n_min=1, n_max=1, separators=[""], children=children, seed=seed
        )

    # def to_json(self):
    #     parent = super().to_json()
    #     parent["combinator_type"] = self._combinator_type
    #     return parent

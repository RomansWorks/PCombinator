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
        seed: Union[int, None] = None,
        children: List[Union[Combinator, str, None]] = [],
        id: str = None,
    ):
        super().__init__(1, 1, "", seed, children, id)

    # def to_json(self):
    #     parent = super().to_json()
    #     parent["combinator_type"] = self._combinator_type
    #     return parent

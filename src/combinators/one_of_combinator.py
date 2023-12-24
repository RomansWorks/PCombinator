from typing import List, Union
from src.combinators.combinator import Combinator
from src.combinators.random_join_combinator import RandomJoinCombinator


class OneOfCombinator(RandomJoinCombinator):
    def __init__(
        self,
        seed: int | None = None,
        children: List[Union[Combinator, str]] = [],
        id: str = None,
    ):
        super().__init__(1, 1, "", seed, children, id)
        self._combinator_type = "one_of"

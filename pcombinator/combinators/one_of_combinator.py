import random
from typing import List, Literal, Union
from pcombinator.combinators.combinator import derived_classes
from pcombinator.combinators.combinator_or_leaf_type import CombinatorOrLeaf
from pcombinator.combinators.random_join_combinator import RandomJoinCombinator


class OneOfCombinator(RandomJoinCombinator):
    """
    On render, this combinator will randomly select one of the children and render it.
    """

    # _combinator_type: Literal["one_of"] = "one_of"

    def __init__(
        self,
        id: str,
        children: List[CombinatorOrLeaf] = [],
        seed: Union[int, None] = None,
    ):
        super().__init__(
            id=id,
            n_min=1,
            n_max=1,
            separators=[""],
            children=children,
            seed=seed,
            random=random.Random(x=seed),
            # combinator_type=__class__.__name__,
        )

    # def to_json(self):
    #     parent = super().to_json()
    #     parent["combinator_type"] = self._combinator_type
    #     return parent


# derived_classes["one_of"] = OneOfCombinator
# derived_classes[OneOfCombinator.__name__] = OneOfCombinator

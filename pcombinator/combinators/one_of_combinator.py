import random
from typing import List, Union
from pcombinator.combinators.combinator import Combinator, derived_classes
from pcombinator.combinators.combinator_or_leaf_type import CombinatorOrLeaf
from pcombinator.combinators.some_of_combinator import SomeOfCombinator
from pcombinator.util.classname import get_fully_qualified_class_name


class OneOfCombinator(SomeOfCombinator):
    """
    A combinator which renders exactly one of its children. Based on RandomJoinCombinator.
    """

    children: List[CombinatorOrLeaf]

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
            separator="",
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

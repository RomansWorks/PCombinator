import json
from pcombinator.combinators.combinator import Combinator, IdTree, derived_classes
from pcombinator.util.classname import get_fully_qualified_class_name


class FixedStringCombinator(Combinator):
    """
    A combinator that renders a fixed string.

    NOTE: This is only necessary when you want to preserve the id of the string in the IdTree. Otherwise you can just use a string as a child of a higher combinator.
    """

    string: str

    def __init__(
        self,
        id: str,
        string: str,
        **kwargs,
    ):
        """
        Initialize a new FixedStringCombinator.

        Args:
            id: The id of the combinator.
            string: The string to render.
        """
        super().__init__(
            id=id,
            combinator_type=kwargs.get("combinator_type")
            or get_fully_qualified_class_name(self.__class__),
        )

        if not isinstance(string, str) or string is None:
            raise ValueError(f"string must be a string, not {type(string)}")

        self.string = string

    def render(self) -> tuple[str, IdTree]:
        """
        Render self, specifically returns the string and an empty IdTree since strings don't have an additional identifier.
        """
        return self.string, {self.id: {}}

    def render_all(self) -> tuple[str, IdTree]:
        """
        Render self, specifically returns the string and an empty IdTree since strings don't have an additional identifier.
        """
        return self.string, {self.id: {}}

    @classmethod
    def from_json(cls, values: dict):
        return cls(
            id=values["id"],
            string=values["string"],
        )


Combinator.register_derived_class(FixedStringCombinator)

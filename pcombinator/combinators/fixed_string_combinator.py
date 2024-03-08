from pydantic import Field
from pcombinator.combinators.combinator import Combinator, IdTree, derived_classes


class FixedStringCombinator(Combinator):
    """
    A combinator that renders a fixed string.

    NOTE: This is only necessary when you want to preserve the id of the string in the IdTree. Otherwise you can just use a string as a child of a higher combinator.
    """

    # _combinator_type: Literal["fixed_string"] = "fixed_string"

    string: str

    def __init__(self, id: str, string: str):
        """
        Initialize a new FixedStringCombinator.

        Args:
            id: The id of the combinator.
            string: The string to render.
        """
        super().__init__(
            id=id,
            string=string,
            # combinator_type=__class__.__name__,
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

    # def to_json(self):
    #     """
    #     Convert self to a json-compatible dictionary.
    #     """
    #     return {
    #         "combinator_type": self._combinator_type,
    #         "id": self.id,
    #         "string": self.string,
    #     }


# derived_classes["fixed_string"] = FixedStringCombinator
# derived_classes[FixedStringCombinator.__name__] = FixedStringCombinator

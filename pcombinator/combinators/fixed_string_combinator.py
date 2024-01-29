from typing import Literal
from pcombinator.combinators.combinator import Combinator, IdTree


class FixedStringCombinator(Combinator):
    """
    A combinator that renders a fixed string.

    NOTE: This is only necessary when you want to preserve the id of the string in the IdTree. Otherwise you can just use a string as a child of a higher combinator.
    """

    _combinator_type: Literal["fixed_string"] = "fixed_string"

    string: str

    def __init__(self, string: str, id: str = None):
        """
        Initialize a new FixedStringCombinator.

        Args:
            string: The string to render.
            id: The id of the combinator.
        """

        super().__init__(id=id)

    def render(self) -> (str, IdTree):
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

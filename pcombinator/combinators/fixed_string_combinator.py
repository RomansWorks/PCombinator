from typing import Literal, Union

from pydantic import Field
from pcombinator.combinators.combinator import Combinator, IdTree


class FixedStringCombinator(Combinator):
    """
    A combinator that renders a fixed string.

    NOTE: This is only necessary when you want to preserve the id of the string in the IdTree. Otherwise you can just use a string as a child of a higher combinator.
    """

    _combinator_type: Literal["fixed_string"] = "fixed_string"

    string: str = Field(...)

    def __init__(self, id: str, string: str):
        """
        Initialize a new FixedStringCombinator.

        Args:
            string: The string to render.
            id: The id of the combinator.
        """
        super().__init__(id=id, string=string)

        self.string = string

    def render(self) -> tuple[str, IdTree]:
        """
        Render self, specifically returns the string and an empty IdTree since strings don't have an additional identifier.
        """
        return self.string, {self._id: {}}

    # def to_json(self):
    #     """
    #     Convert self to a json-compatible dictionary.
    #     """
    #     return {
    #         "combinator_type": self._combinator_type,
    #         "id": self.id,
    #         "string": self.string,
    #     }

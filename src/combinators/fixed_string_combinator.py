from src.combinators.combinator import Combinator, IdTree


class FixedStringCombinator(Combinator):
    def __init__(self, string: str, id: str = None):
        super().__init__(id=id)
        self._combinator_type = "fixed_string"
        self.string = string

    def render(self) -> (str, IdTree):
        return self.string, {self.id: {}}

import unittest

from pcombinator.combinators.combinator import Combinator, render_children
from pcombinator.combinators.fixed_string_combinator import FixedStringCombinator


class CombinatorTest(unittest.TestCase):
    def test_render_children(self):
        # Arrange
        children = ["abc", "def", FixedStringCombinator(id="id1", string="ghi")]

        # Act
        rendered_text, id_tree = render_children(children)

        # Assert
        self.assertEqual(rendered_text, ["abc", "def", "ghi"])
        self.assertEqual(id_tree, {"id1": {}})


if __name__ == "__main__":
    unittest.main()

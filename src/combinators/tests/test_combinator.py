import unittest
from src.combinators.combinator import Combinator
from src.combinators.fixed_string_combinator import FixedStringCombinator


class CombinatorTest(unittest.TestCase):
    def test_render(self):
        combinator = Combinator()
        with self.assertRaises(NotImplementedError):
            combinator.render()

    def test_render_children(self):
        # Arrange
        children = ["abc", "def", FixedStringCombinator("ghi")]
        combinator = Combinator("id1")

        # Act
        rendered_text, id_tree = combinator.render_children(children)

        # Assert
        self.assertEqual(rendered_text, [])
        self.assertEqual(id_tree, {})


if __name__ == "__main__":
    unittest.main()

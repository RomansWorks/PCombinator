import unittest
from pcombinator.combinators.fixed_string_combinator import FixedStringCombinator


class FixedStringCombinatorTest(unittest.TestCase):

    def test_render_path(self):
        # Arrange
        string = "Hello, World!"
        combinator = FixedStringCombinator(id="id1", string=string)

        # Act
        paths = combinator.generate_paths()
        rendered = combinator.render_path(paths[0])

        # Assert
        self.assertEqual(rendered, string)

    def test_generate_paths(self):
        # Arrange
        combinator = FixedStringCombinator(id="id1", string="Hello, World!")

        # Act
        paths = combinator.generate_paths()

        # Assert
        self.assertEqual(paths, [{"id1": {}}])


if __name__ == "__main__":
    unittest.main()

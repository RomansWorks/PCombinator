import unittest
from src.combinators.fixed_string_combinator import FixedStringCombinator


class FixedStringCombinatorTest(unittest.TestCase):
    def test_render(self):
        string = "Hello, World!"
        combinator = FixedStringCombinator(string)
        expected_output = (string, {combinator.id: {}})
        self.assertEqual(combinator.render(), expected_output)


if __name__ == "__main__":
    unittest.main()

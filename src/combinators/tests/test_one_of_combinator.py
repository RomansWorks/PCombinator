import unittest
from src.combinators.one_of_combinator import OneOfCombinator
from src.combinators.combinator import Combinator


class OneOfCombinatorTests(unittest.TestCase):
    def test_initialization(self):
        one_of_combinator = OneOfCombinator(
            seed=123, children=["abc", "def"], id="test_id"
        )
        self.assertEqual(one_of_combinator._combinator_type, "one_of")
        self.assertEqual(one_of_combinator._min_children, 1)
        self.assertEqual(one_of_combinator._max_children, 1)
        self.assertEqual(one_of_combinator._seed, 123)
        self.assertEqual(one_of_combinator._children, ["abc", "def"])
        self.assertEqual(one_of_combinator._id, "test_id")

    def test_default_values(self):
        one_of_combinator = OneOfCombinator()
        self.assertEqual(one_of_combinator._combinator_type, "one_of")
        self.assertEqual(one_of_combinator._min_children, 1)
        self.assertEqual(one_of_combinator._max_children, 1)
        self.assertIsNone(one_of_combinator._seed)
        self.assertEqual(one_of_combinator._children, [])
        self.assertIsNone(one_of_combinator._id)

    # Add more test cases as needed


if __name__ == "__main__":
    unittest.main()

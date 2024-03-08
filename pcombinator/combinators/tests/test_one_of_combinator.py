import unittest
from pcombinator.combinators.one_of_combinator import OneOfCombinator
from pcombinator.combinators.combinator import Combinator


class OneOfCombinatorTests(unittest.TestCase):
    def test_initialization(self):
        one_of_combinator = OneOfCombinator(
            id="id_1",
            seed=123,
            children=["abc", "def"],
        )
        self.assertEqual(
            one_of_combinator.combinator_type,
            "pcombinator.combinators.one_of_combinator.type",
        )
        self.assertEqual(one_of_combinator.n_min, 1)
        self.assertEqual(one_of_combinator.n_max, 1)
        self.assertEqual(one_of_combinator.children, ["abc", "def"])
        self.assertEqual(one_of_combinator.id, "id_1")

    def test_default_values(self):
        one_of_combinator = OneOfCombinator(id="id_1")
        self.assertEqual(
            one_of_combinator.combinator_type,
            "pcombinator.combinators.one_of_combinator.type",
        )
        self.assertEqual(one_of_combinator.n_min, 1)
        self.assertEqual(one_of_combinator.n_max, 1)
        self.assertEqual(one_of_combinator.children, [])
        self.assertEqual(one_of_combinator.id, "id_1")


if __name__ == "__main__":
    unittest.main()

import unittest
from unittest.mock import patch
from pcombinator.combinators.random_join_combinator import RandomJoinCombinator
from pcombinator.combinators.combinator import render_children


class RandomJoinCombinatorTests(unittest.TestCase):
    def test_render(self):
        random_join_combinator = RandomJoinCombinator(
            n_min=2,
            n_max=4,
            children=["abc", "def", "ghi"],
            separators=["-"],
            seed=1007,
            id="test_combinator_id",
        )
        rendered, id_tree = random_join_combinator.render()

        self.assertEqual(
            rendered, "ghi-abc"
        )  # Note this is not a random result, but a result of the seed
        self.assertEqual(id_tree, {"test_combinator_id": {}})


if __name__ == "__main__":
    unittest.main()

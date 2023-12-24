import unittest
from src.combinators.random_join_combinator import RandomJoinCombinator
from src.combinators.template_combinator import TemplateCombinator


class TemplateCombinatorTests(unittest.TestCase):
    def test_render(self):
        # Create a TemplateCombinator instance
        template_combinator = TemplateCombinator(
            "{{role}}\n{{task}}\n{{question}}\n",
            {
                "role": "value_1",
                "task": "value_2",
                "question": RandomJoinCombinator(1, 1, ["option_1"], "\n"),
            },
        )

        # Render
        result, id_tree = template_combinator.render()

        # Check the result
        self.assertEqual(
            result,
            "value_1\nvalue_2\noption_1\n",
        )


if __name__ == "__main__":
    unittest.main()

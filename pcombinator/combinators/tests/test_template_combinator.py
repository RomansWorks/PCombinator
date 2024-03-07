import unittest
from pcombinator.combinators.fixed_string_combinator import FixedStringCombinator

from pcombinator.combinators.random_join_combinator import RandomJoinCombinator
from pcombinator.combinators.template_combinator import Jinja2TemplateCombinator


class TemplateCombinatorTests(unittest.TestCase):
    def test_render(self):
        # Create a TemplateCombinator instance
        template_source = "{{role}}\n{{task}}\n{{question}}\n"

        template_combinator = Jinja2TemplateCombinator(
            id="template_1",
            template_source=template_source,
            children={
                "role": "value_1_of_role",
                "task": "value_1_of_task",
                "question": RandomJoinCombinator(
                    id="question_randomizer_1",
                    n_max=1,
                    n_min=1,
                    children=["option_1"],
                    separators=["\n"],
                ),
            },
        )

        # Render
        result, id_tree = template_combinator.render()

        # Check the result
        self.assertEqual(
            result,
            "value_1_of_role\nvalue_1_of_task\noption_1",
        )

        # Check the id_tree
        self.assertEqual(
            id_tree,
            {
                "template_1": {
                    "role": {},
                    "task": {},
                    "question": {"question_randomizer_1": {}},
                }
            },
        )


if __name__ == "__main__":
    unittest.main()

import unittest

from pcombinator.combinators.combinator import Combinator, render_children
from pcombinator.combinators.fixed_string_combinator import FixedStringCombinator
from pcombinator.combinators.random_join_combinator import RandomJoinCombinator
from pcombinator.combinators.template_combinator import Jinja2TemplateCombinator


class CombinatorTest(unittest.TestCase):
    def test_render_children(self):
        # Arrange
        children = ["abc", "def", FixedStringCombinator(id="id1", string="ghi")]

        # Act
        rendered_text, id_tree = render_children(children)

        # Assert
        self.assertEqual(rendered_text, ["abc", "def", "ghi"])
        self.assertEqual(id_tree, {"id1": {}})

    def test_json_peristence(self):
        # Arrange
        seed = 1007
        template_source = "{{role}}\n{{task}}\n{{question}}\n"
        template_combinator = Jinja2TemplateCombinator(
            template_source=template_source,
            children={
                "role": FixedStringCombinator("role_id", "value_1"),
                "task": "task_value",
                "question": RandomJoinCombinator(
                    n_max=1,
                    n_min=1,
                    children=["option_1"],
                    separators=["\n"],
                    seed=seed,
                    id="question_randomizer_1",
                ),
            },
            id="template_1",
        )

        # Act
        json_str = template_combinator.to_json()
        loaded_combinator = Combinator.from_json(json_str)

        print("=" * 80)
        print(template_combinator)
        print("_" * 80)
        print(loaded_combinator)
        print("=" * 80)

        # Assert
        self.assertEqual(loaded_combinator, template_combinator)


if __name__ == "__main__":
    unittest.main()

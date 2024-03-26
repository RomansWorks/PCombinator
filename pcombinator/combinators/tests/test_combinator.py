import unittest

from pcombinator.combinators.combinator import Combinator
from pcombinator.combinators.named_string import NamedString
from pcombinator.combinators.join_some_of import JoinSomeOf
from pcombinator.combinators.jinja2_template import Jinja2Template


class CombinatorTest(unittest.TestCase):

    def test_json_peristence(self):
        # Arrange
        seed = 1007
        template_source = "{{role}}\n{{task}}\n{{question}}\n"
        template_combinator = Jinja2Template(
            template_source=template_source,
            children={
                "role": NamedString("role_id", "value_1"),
                "task": "task_value",
                "question": JoinSomeOf(
                    n_max=1,
                    n_min=1,
                    children=["option_1"],
                    separator="\n",
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
        # We'll convert both to text and compare them
        self.assertEqual(template_combinator.to_json(), loaded_combinator.to_json())


if __name__ == "__main__":
    unittest.main()

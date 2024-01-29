import json
import tempfile
import unittest
import jinja2
from pcombinator.combinators.random_join_combinator import RandomJoinCombinator

from pcombinator.combinators.template_combinator import Jinja2TemplateCombinator
from pcombinator.persistence.combinators_file import CombinatorsFile


class TestCombinatorsFile(unittest.TestCase):
    def test_persist_and_load(self):
        seed = 1007

        # Create a TemplateCombinator instance
        template_source = "{{role}}\n{{task}}\n{{question}}\n"

        template_combinator = Jinja2TemplateCombinator(
            template_source=template_source,
            children={
                "role": "value_1",
                "task": "value_2",
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

        # Store
        combinators_file = CombinatorsFile(
            version="0.0.1",
            seed=seed,
            root_combinator=template_combinator,
        )

        with tempfile.NamedTemporaryFile() as f:
            for format in ["json", "pickle"]:
                if format == "json":
                    combinators_file.to_json_file(f.name)
                    loaded_combinators_file = CombinatorsFile.from_json_file(f.name)
                    print(loaded_combinators_file)
                else:
                    combinators_file.to_pickle(f.name)
                    loaded_combinators_file = CombinatorsFile.from_pickle(f.name)

                # Get the root combinator and check whether it is the same as the original
                loaded_template_combinator = loaded_combinators_file.root_combinator
                print(loaded_template_combinator)
                self.assertEqual(
                    loaded_template_combinator.get_id(),
                    template_combinator.get_id(),
                )

                # Get the children of the root combinator and check whether they are the same as the original
                loaded_children = loaded_template_combinator.get_children()
                original_children = template_combinator.get_children()

                self.assertEqual(len(loaded_children), len(original_children))

                for i, loaded_child in enumerate(loaded_children):
                    original_child = original_children[i]
                    self.assertEqual(
                        loaded_child.get_id(),
                        original_child.get_id(),
                    )


if __name__ == "__main__":
    unittest.main()

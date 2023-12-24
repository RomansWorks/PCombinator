import unittest
from src.combinators.template_combinator import TemplateCombinator


class TemplateCombinatorTests(unittest.TestCase):
    def test_render(self):
        # Create a TemplateCombinator instance
        template_combinator = TemplateCombinator()

        # Set up the children dictionary
        template_combinator.children = {
            "key1": "value1",
            "key2": "value2",
            "key3": "value3",
        }

        # Set up the template
        template_combinator.template = "Hello {key1}, {key2}, {key3}!"

        # Call the render method
        result, id_tree = template_combinator.render()

        # Check the result
        self.assertEqual(result, "Hello value1, value2, value3!")

        # Check the id tree
        expected_id_tree = {
            template_combinator.id: {"key1": {}, "key2": {}, "key3": {}}
        }
        self.assertEqual(id_tree, expected_id_tree)

    # Add more test cases as needed


if __name__ == "__main__":
    unittest.main()

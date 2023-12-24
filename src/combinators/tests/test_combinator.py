import unittest
from combinator import Combinator


class CombinatorTest(unittest.TestCase):
    def test_render(self):
        combinator = Combinator()
        with self.assertRaises(NotImplementedError):
            combinator.render()

    def test_render_children(self):
        with self.assertRaises(NotImplementedError):
            Combinator.render_children([])


if __name__ == "__main__":
    unittest.main()

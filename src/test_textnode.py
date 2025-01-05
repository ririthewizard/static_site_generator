import unittest

from textnode import TextNode, TextType

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_print_repr(self):
        node = TextNode("This is a test node", TextType.ITALIC)
        printed = node.__repr__()
        expected = "TextNode(This is a test node, TextType.ITALIC, None)"
        self.assertEqual(printed, expected)

if __name__ == "__main__":
    unittest.main()
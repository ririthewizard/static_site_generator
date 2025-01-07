import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        html_node = HTMLNode("p", "This is an html node", "", {"href": "https://www.google.com"})
        expected = " href= https://www.google.com"
        self.assertEqual(html_node.props_to_html(), expected)
import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def return_val_err(self):
        leaf_node = LeafNode("a")
        self.assertRaises(ValueError, leaf_node.to_html)
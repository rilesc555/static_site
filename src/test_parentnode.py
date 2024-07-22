from parentnode import ParentNode
from leafnode import LeafNode
import unittest

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode("p",
                          children=[
                              LeafNode("b", value="Bold text"),
                              LeafNode(value="Normal text"),
                              LeafNode("i", value="italic text"),
                              LeafNode(value="Normal text"),
                          ]
                          )
        
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(expected, node.to_html())

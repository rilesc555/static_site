from parentnode import ParentNode
from leafnode import LeafNode
import unittest

class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(tag="p",
                          children=[
                              LeafNode(tag="b", value="Bold text"),
                              LeafNode(tag=None, value="Normal text"),
                              LeafNode(tag="i", value="italic text"),
                              LeafNode(tag=None, value="Normal text"),
                          ],
                          )
        
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(expected, node.to_html())

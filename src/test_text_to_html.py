from re import L
import utils
import unittest
from textnode import TextNode
from leafnode import LeafNode

class TestTextToHtml(unittest.TestCase):
    def test_text_to_html(self):
        text = "This is a text node"
        type = "bold"
        expected = LeafNode("b", text)
        testNode = TextNode(text, type)

        self.assertEqual(expected, utils.text_node_to_html_node(testNode))
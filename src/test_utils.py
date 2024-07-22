from utils import *
import unittest
from textnode import TextNode
from leafnode import LeafNode

class TestUtils(unittest.TestCase):
    def test_text_to_html(self):
        text = "This is a text node"
        type = "bold"
        expected = LeafNode("b", value=text)
        testNode = TextNode(text, type)

        self.assertEqual(expected, text_node_to_html_node(testNode))

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", "text", "bold")
        new_nodes = split_nodes_delimiter([node], "`", "code")

        expected = [
            TextNode("This is text with a ", "text", "bold"),
            TextNode("code block", "text", "bold", "code"),
            TextNode(" word", "text", "bold"),
        ]

        self.assertEqual(expected, new_nodes)

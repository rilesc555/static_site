from tkinter import W
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
    
    def test_extract_markdown_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        actual = extract_first_image(text)
        expected = ("rick roll", "https://i.imgur.com/aKaOqIh.gif")

        self.assertEqual(actual, expected)

    def test_split_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_text, text_type_image, url="https://i.imgur.com/zjjcJKZ.png"),
            ],
            new_nodes,
        )

    def test_split_image_single(self):
        node = TextNode(
            "![image](https://www.example.com/image.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("image", text_type_text, text_type_image, url="https://www.example.com/image.png"),
            ],
            new_nodes,
        )

    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_text, text_type_image, url="https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_text, text_type_image, url="https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def test_split_links(self):
        node = TextNode(
            "This is text with a [link](https://boot.dev) and [another link](https://blog.boot.dev) with text that follows",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("link", text_type_text, text_type_link, url="https://boot.dev"),
                TextNode(" and ", text_type_text),
                TextNode("another link", text_type_text, text_type_link, url="https://blog.boot.dev"),
                TextNode(" with text that follows", text_type_text),
            ],
            new_nodes,
        )
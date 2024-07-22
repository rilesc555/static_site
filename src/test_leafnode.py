import unittest
from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_props_to_html(self):
        value = "Click me!"
        tags = "a"
        props = {"href": "https://www.google.com"}
        testLeaf = LeafNode(tags, value=value, props=props)

        expected = "<a href=\"https://www.google.com\">Click me!</a>"

        self.assertEqual(testLeaf.to_html(), expected)

    def test_no_tag_to_html(self):
        value = "Click me!"
        props = {"href": "https://www.google.com"}
        testLeaf = LeafNode(value=value, props=props)

        self.assertEqual(value, testLeaf.to_html())
        
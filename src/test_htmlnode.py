import unittest
from src.htmlnode import HTMLNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        Props = {
            "href": "https://www.google.com", 
            "target": "_blank",
        }
        expected = " href=\"https://www.google.com\" target=\"_blank\""
        test_node = HTMLNode(props=Props)
        self.assertEqual(test_node.props_to_html(), expected)

    def test_to_html(self):
        testNode = HTMLNode()
        with self.assertRaises(NotImplementedError):
            testNode.to_html()
    
if __name__=="__main__":
    unittest.main()
import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props_dict = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=props_dict)
        s = node.props_to_html()
        self.assertEqual(s, "href=\"https://www.google.com\" target=\"_blank\"")

    def test_leaftnode_to_html_value_error(self):
        node = LeafNode()
        self.assertRaises(ValueError)

    def test_leaftnode_to_html_return_plain_text(self):
        node = LeafNode(value="test")
        self.assertEqual(node.to_html(), "test")

    def test_leaftnode_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_leaftnode_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

if __name__ == "__main__":
    unittest.main()
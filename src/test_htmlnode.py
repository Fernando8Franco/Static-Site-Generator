import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    ################
    # HTMLNode tests
    ################
    def test_props_to_html(self):
        props_dict = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=props_dict)
        s = node.props_to_html()
        self.assertEqual(s, " href=\"https://www.google.com\" target=\"_blank\"")

    ################
    # LeafNode tests
    ################
    def test_leaftnode_to_html_value_error(self):
        with self.assertRaises(ValueError):
            node = LeafNode(None, None, None)
            node.to_html()

    def test_leaftnode_to_html_return_plain_text(self):
        node = LeafNode(None, "test", None)
        self.assertEqual(node.to_html(), "test")

    def test_leaftnode_to_html(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")

    def test_leaftnode_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.", None)
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")

    ##################
    # ParentNode tests
    ##################
    def test_parentnode_to_html_value_error_children(self):
        with self.assertRaises(ValueError):
            node = ParentNode("p", None, None)
            node.to_html()

    def test_parentnode_to_html_value_error_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(None, LeafNode(None, "Hello"))
            node.to_html()

    def test_parentnode_to_html_value_error_tag(self):
        with self.assertRaises(ValueError):
            node = ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold"),
                        LeafNode(None, "Normal"),
                        ParentNode(
                            "p",
                            [
                                LeafNode("i", "Italic"),
                                ParentNode(
                                    "",
                                    [
                                        LeafNode(None, "Normal")
                                    ]
                                )
                            ]
                        )
                    ]
                )
            node.to_html()

    def test_parentnode_to_html(self):
        node = ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ]
                )
        self.assertEqual(node.to_html(), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

    def test_parentnode_to_html(self):
        node = ParentNode(
                    "p",
                    [
                        LeafNode("b", "Bold"),
                        LeafNode(None, "Normal"),
                        ParentNode(
                            "p",
                            [
                                LeafNode("i", "Italic"),
                                ParentNode(
                                    "h1",
                                    [
                                        LeafNode(None, "Normal")
                                    ]
                                )
                            ]
                        )
                    ]
                )
        self.assertEqual(node.to_html(), "<p><b>Bold</b>Normal<p><i>Italic</i><h1>Normal</h1></p></p>")

if __name__ == "__main__":
    unittest.main()
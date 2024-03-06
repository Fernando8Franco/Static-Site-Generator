import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props_dict = {"href": "https://www.google.com", "target": "_blank"}
        node = HTMLNode(props=props_dict)
        s = node.props_to_html()
        self.assertEqual(s, "href=\"https://www.google.com\" target=\"_blank\"")

if __name__ == "__main__":
    unittest.main()
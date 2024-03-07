import unittest
from htmlnode import LeafNode
from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_url_none(self):
        node = TextNode("Text node", "italic")
        self.assertIsNone(node.url)

    def test_text_type_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node.text_type, node2.text_type)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "italic")
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node_text(self):
        node = TextNode('Text', 'text')
        leafNode = text_node_to_html_node(node)
        self.assertEqual(leafNode, LeafNode(None, 'Text'))
    
    def test_text_node_to_html_node_bold(self):
        node = TextNode('Text', 'bold')
        leafNode = text_node_to_html_node(node)
        self.assertEqual(leafNode, LeafNode('b', 'Text'))

    def test_text_node_to_html_node_italic(self):
        node = TextNode('Text', 'italic')
        leafNode = text_node_to_html_node(node)
        self.assertEqual(leafNode, LeafNode('i', 'Text'))

    def test_text_node_to_html_node_code(self):
        node = TextNode('Text', 'code')
        leafNode = text_node_to_html_node(node)
        self.assertEqual(leafNode, LeafNode('code', 'Text'))

    def test_text_node_to_html_node_link(self):
        node = TextNode('Text', 'link', "https://www.google.com")
        leafNode = text_node_to_html_node(node)
        self.assertEqual(leafNode, LeafNode('a', 'Text', {"href": "https://www.google.com"}))

    def test_text_node_to_html_node_image(self):
        node = TextNode('google', 'image', "https://www.google.com")
        leafNode = text_node_to_html_node(node)
        self.assertEqual(leafNode, LeafNode('img', '', {"src": "https://www.google.com", "alt": "google"}))

    def test_text_node_to_html_exception(self):
        with self.assertRaises(Exception):
            node = TextNode('Text', 'headliner')
            leafNode = text_node_to_html_node(node)

if __name__ == "__main__":
    unittest.main()
import unittest

from inline_markdown import split_nodes_delimiter
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ]
        )

    def test_split_nodes_delimiter(self):
        node = TextNode("This is text with a **bold text** word **bold**", text_type_text)
        new_nodes = split_nodes_delimiter([node], "**", text_type_bold)
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("bold text", text_type_bold),
                TextNode(" word ", text_type_text),
                TextNode("bold", text_type_bold),
            ]
        )

    def test_split_nodes_delimiter_exception(self):
        with self.assertRaises(Exception):
            node = TextNode("This is text with a `code block word", text_type_text)
            new_nodes = split_nodes_delimiter([node], "`", text_type_code)

    def test_split_nodes_delimiter_multiple_delimiters(self):
        node = TextNode("This is text with a `code block` *word*", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        new_new_nodes = split_nodes_delimiter(new_nodes, "*", text_type_italic)
        self.assertListEqual(
            new_new_nodes,
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" ", text_type_text),
                TextNode("word", text_type_italic),
            ]
        )


if __name__ == "__main__":
    unittest.main()
import unittest

from inline_markdown import split_nodes_delimiter, extract_markdown_images, extract_markdown_links
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image

class TestInlineMarkdown(unittest.TestCase):
    #####
    ## TEST FUNCTION SPLIT NODE DELIMITER
    #####
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

    #####
    ## TEST FUNCTION EXTRACT MARKDOWN IMAGES
    #####
    def test_extract_markdown_images(self):
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
        images = extract_markdown_images(text)
        self.assertListEqual(
            images,
            [
                ("image", "https://i.imgur.com/zjjcJKZ.png"),
                ("another", "https://i.imgur.com/dfsdkjfd.png")
            ]
        )
        
    #####
    ## TEST FUNCTION EXTRACT MARKDOWN LINKS
    #####
    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        images = extract_markdown_links(text)
        self.assertListEqual(
            images,
            [
                ("link", "https://www.example.com"),
                ("another", "https://www.example.com/another")
            ]
        )

if __name__ == "__main__":
    unittest.main()
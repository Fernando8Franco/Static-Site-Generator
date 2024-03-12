import unittest

from inline_markdown import (split_nodes_delimiter, 
                             extract_markdown_images, 
                             extract_markdown_links,
                             split_nodes_image,
                             split_nodes_link,
                             text_to_textnodes)
from textnode import (TextNode, 
                      text_type_text, 
                      text_type_bold, 
                      text_type_italic, 
                      text_type_code, 
                      text_type_link, 
                      text_type_image)

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

    #####
    ## TEST FUNCTION SPLIT NODES IMAGES
    #####
    def test_split_nodes_image(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second image", text_type_image, "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        )

    #####
    ## TEST FUNCTION SPLIT NODES LINKS
    #####
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with an [link](https://i.imgur.com/zjjcJKZ.png) and another [second link](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            new_nodes,
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("link", text_type_link, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", text_type_text),
                TextNode(
                    "second link", text_type_link, "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        )

    def test_split_nodes_link_and_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and link [link](https://i.imgur.com/3elNhQu.png)",
            text_type_text,
        )
        nodes_images = split_nodes_image([node])
        node_links = split_nodes_link(nodes_images)
        self.assertListEqual(
            node_links,
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and link ", text_type_text),
                TextNode(
                    "link", text_type_link, "https://i.imgur.com/3elNhQu.png"
                ),
            ]
        )

    #####
    ## TEST TEXT TO TEXTNODES
    #####
    def test_text_to_textnodes(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        nodes = text_to_textnodes(text)
        self.assertListEqual(
            nodes,
            [
                TextNode("This is ", text_type_text),
                TextNode("text", text_type_bold),
                TextNode(" with an ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word and a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" and an ", text_type_text),
                TextNode("image", text_type_image, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and a ", text_type_text),
                TextNode("link", text_type_link, "https://boot.dev"),
            ]
        )
    

if __name__ == "__main__":
    unittest.main()
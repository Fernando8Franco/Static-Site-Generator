import unittest

from block_markdown import (markdown_to_blocks,
                            block_to_block_type,
                            markdown_to_html_node,
                            block_type_paragraph,
                            block_type_heading,
                            block_type_code,
                            block_type_quote,
                            block_type_unordered_list,
                            block_type_ordered_list)

from htmlnode import ParentNode, LeafNode

class TestBlockMarkdown(unittest.TestCase):
    #####
    # TEST MARKDOWN TO BLOCKS FUNCTION
    #####
    def test_markdown_to_blocks(self):
        text = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

        blocks = markdown_to_blocks(text)
        self.assertListEqual(
            blocks,
            [
            'This is **bolded** paragraph', 
            'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', 
            '* This is a list\n* with items'
            ]
        )

    def test_markdown_to_blocks(self):
        text = """
This is **bolded** paragraph



This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

        blocks = markdown_to_blocks(text)
        self.assertListEqual(
            blocks,
            [
            'This is **bolded** paragraph', 
            'This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line', 
            '* This is a list\n* with items'
            ]
        )

    #####
    # TEST BLOCK TO BLOCK TYPE FUNCTION
    #####
    def test_block_to_block_type_paragraph(self):
        type = block_to_block_type("This is a paragraph")
        self.assertEqual(type, block_type_paragraph)

    def test_block_to_block_type_heading(self):
        test_cases = [
            ("# This is a heading", block_type_heading),
            ("## This is a heading", block_type_heading),
            ("### This is a heading", block_type_heading),
            ("#### This is a heading", block_type_heading),
            ("##### This is a heading", block_type_heading),
            ("###### This is a heading", block_type_heading)
        ]
        for input_text, expected_type in test_cases:
            with self.subTest(input_text=input_text, expected_type=expected_type):
                type = block_to_block_type(input_text)
                self.assertEqual(type, expected_type)

    def test_block_to_block_type_code(self):
        test_cases = [
            ("```This is a code```", block_type_code),
            ("```This is a code\nMore code```", block_type_code),
            ("``This is a heading``", block_type_paragraph)
        ]
        for input_text, expected_type in test_cases:
            with self.subTest(input_text=input_text, expected_type=expected_type):
                type = block_to_block_type(input_text)
                self.assertEqual(type, expected_type)

    def test_block_to_block_type_quote(self):
        test_cases = [
            (">quote\n>quote\n>quote\n>quote", block_type_quote),
            (">quote", block_type_quote),
            (">quote\nNot a quote", block_type_paragraph),
        ]
        for input_text, expected_type in test_cases:
            with self.subTest(input_text=input_text, expected_type=expected_type):
                type = block_to_block_type(input_text)
                self.assertEqual(type, expected_type)

    def test_block_to_block_type_unordered_list(self):
        test_cases = [
            ("* unlist\n* unlist\n* unlist", block_type_unordered_list),
            ("- unlist", block_type_unordered_list),
            ("- quote\nNot a list", block_type_paragraph),
        ]
        for input_text, expected_type in test_cases:
            with self.subTest(input_text=input_text, expected_type=expected_type):
                type = block_to_block_type(input_text)
                self.assertEqual(type, expected_type)

    def test_block_to_block_type_ordered_list(self):
        test_cases = [
            ("1. orlist\n2. orlist\n3. orlist", block_type_ordered_list),
            ("1. orlist", block_type_ordered_list),
            ("1. orlist\n3. orlist", block_type_paragraph),
        ]
        for input_text, expected_type in test_cases:
            with self.subTest(input_text=input_text, expected_type=expected_type):
                type = block_to_block_type(input_text)
                self.assertEqual(type, expected_type)

    #####
    # TEST MARKDOWN TO HTML NODE
    #####
    def test_block_to_html_node(self):
        text = """
This is **bolded** paragraph
"""

        node = markdown_to_html_node(text)
        html = node.to_html()

        self.assertEqual(
            html,
            '<div><p>This is <b>bolded</b> paragraph</p></div>'
        )

    def test_block_to_html_node(self):
        text = """
- This is a list
- with items
- and *more* items

1. This is an `ordered` list
2. with items
3. and more items
"""

        node = markdown_to_html_node(text)
        html = node.to_html()

        self.assertEqual(
            html,
            '<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>'
        )

    def test_block_to_html_node1(self):
        text = """
# Header1

## Header2

paragraph

```
code
code
```

>Quote
>Quote

* list
* *list*

1. o list
"""

        node = markdown_to_html_node(text)
        html = node.to_html()

        self.assertEqual(
            html,
            """<div><h1>Header1</h1><h2>Header2</h2><p>paragraph</p><pre><code>
code
code
</code></pre><blockquote>Quote Quote</blockquote><ul><li>list</li><li><i>list</i></li></ul><ol><li>o list</li></ol></div>"""
        )

    def test_block_to_html_node(self):
        text = """
####### Header
"""

        node = markdown_to_html_node(text)
        html = node.to_html()

        self.assertEqual(
            html,
            '<div><p>####### Header</p></div>'
        )

if __name__ == "__main__":
    unittest.main()
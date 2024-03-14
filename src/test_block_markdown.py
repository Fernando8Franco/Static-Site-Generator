import unittest

from block_markdown import (markdown_to_blocks,
                            block_to_block_type,
                            block_type_paragraph,
                            block_type_heading,
                            block_type_code,
                            block_type_quote,
                            block_type_unordered_list,
                            block_type_ordered_list)

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

if __name__ == "__main__":
    unittest.main()
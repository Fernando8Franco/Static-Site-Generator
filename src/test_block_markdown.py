import unittest

from block_markdown import (markdown_to_blocks)

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

if __name__ == "__main__":
    unittest.main()
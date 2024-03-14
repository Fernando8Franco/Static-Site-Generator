import re
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []

    for block in blocks:
        if block == "":
            continue
        filtered_blocks.append(block.strip())

    return filtered_blocks

def block_to_block_type(block_text):
    pattern_heading = r'^#{1,6}\s.+$'
    if re.match(pattern_heading, block_text):
        return block_type_heading
    
    if block_text[:3] == '```' and block_text[-3:] == '```':
        return block_type_code
    
    lines = block_text.splitlines()
    
    if block_text.startswith('>'):
        for line in lines:
            if not line.startswith('>'):
                return block_type_paragraph
        
        return block_type_quote
    
    if block_text.startswith('* '):
        for line in lines:
            if not line.startswith('* '):
                return block_type_paragraph
        
        return block_type_unordered_list
    
    if block_text.startswith('- '):
        for line in lines:
            if not line.startswith('- '):
                return block_type_paragraph
        
        return block_type_unordered_list
    
    if block_text.startswith('1. '):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1

        return block_type_ordered_list


    return block_type_paragraph
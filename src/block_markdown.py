import re
from textnode import text_node_to_html_node
from inline_markdown import text_to_textnodes
from htmlnode import ParentNode

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

def text_to_html_node(text):
    leaf_nodes = []
    text_nodes = text_to_textnodes(text)

    for text_node in text_nodes:
        leaf_nodes.append(text_node_to_html_node(text_node))

    return leaf_nodes

def markdown_to_html_node(markdown):
    markdown_blocks = markdown_to_blocks(markdown)

    for block in markdown_blocks:
        if block_to_block_type(block) == block_type_paragraph:
            lines = block.splitlines()
            paragraph = " ".join(lines)

            html_nodes = text_to_html_node(paragraph)
            
            return ParentNode('p', html_nodes)

        if block_to_block_type(block) == block_type_heading:
            if '\n' in block:
                raise Exception("Invalid Markdow Sytax: Headers must be separated")
            
            start = None
            for i in range(1, 7):
                if block.startswith("#"*i+" "):
                    level = i
                    break

            if not start:
                raise ValueError('ValueError: Not valid header')

            html_nodes = text_to_html_node(block[level + 1:])

            return ParentNode(f"h{level}", html_nodes)

        if block_to_block_type(block) == block_type_code:
            html_nodes = text_to_html_node(block[3:-3])
            code = ParentNode('code', html_nodes)

            return ParentNode('pre', code)

        if block_to_block_type(block) == block_type_quote:
            lines = block.splitlines()
            paragraph = " ".join(block.replace(">", "").splitlines())

            html_nodes = text_to_html_node(paragraph)

            return ParentNode('blockquote', html_nodes)

        if block_to_block_type(block) == block_type_unordered_list:
            lines = block.splitlines()
            ul_nodes = []

            for line in lines:
                html_nodes = text_to_html_node(line[2:])
                ul_nodes.append(ParentNode("li", html_nodes))

            return ParentNode("ul", ul_nodes)
        
        if block_to_block_type(block) == block_type_ordered_list:
            lines = block.splitlines()
            ol_nodes = []

            for line in lines:
                html_nodes = text_to_html_node(line[2:])
                ol_nodes.append(ParentNode("li", html_nodes))

            return ParentNode("ol", ol_nodes)
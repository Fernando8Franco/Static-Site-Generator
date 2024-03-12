import re
from textnode import TextNode, text_type_text, text_type_bold, text_type_italic, text_type_code, text_type_link, text_type_image

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        
        split_nodes = []
        sections = old_node.text.split(delimiter)

        if len(sections) % 2 == 0:
            raise Exception("Invalid Markdow Sytax: Closing delimiter not found")
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))

        new_nodes.extend(split_nodes)

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        images_tup = extract_markdown_images(original_text)
        if not images_tup:
            new_nodes.append(old_node)
            continue

        for image_tup in images_tup:
            sections = original_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))

            new_nodes.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue

        original_text = old_node.text
        links_tup = extract_markdown_links(original_text)
        if not links_tup:
            new_nodes.append(old_node)
            continue

        for link_tup in links_tup:
            sections = original_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            
            if sections[0] != "":
                new_nodes.append(TextNode(sections[0], text_type_text))

            new_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
            original_text = sections[1]

        if original_text != "":
            new_nodes.append(TextNode(original_text, text_type_text))

    return new_nodes

def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, text)
    return matches

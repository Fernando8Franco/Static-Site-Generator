from htmlnode import LeafNode

text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

class TextNode:
    def __init__(self, text=None, text_type=None, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, o):
        if not isinstance(o, TextNode):
            return False
        
        return (self.text == o.text and
                self.text_type == o.text_type and
                self.url == o.url)
        
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
    
def text_node_to_html_node(tex_node):
    if tex_node.text_type == text_type_text:
        return LeafNode(None, tex_node.text)
    if tex_node.text_type == text_type_bold:
        return LeafNode('b', tex_node.text)
    if tex_node.text_type == text_type_italic:
        return LeafNode('i', tex_node.text)
    if tex_node.text_type == text_type_code:
        return LeafNode('code', tex_node.text)
    if tex_node.text_type == text_type_link:
        return LeafNode('a', tex_node.text, {"href": tex_node.url})
    if tex_node.text_type == text_type_image:
        return LeafNode('img', '', {"src": tex_node.url, "alt": tex_node.text})
    
    raise Exception(f"Invalid text type: {tex_node.text_type}")
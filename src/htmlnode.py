class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        if (not self.props):
            return ""

        porps_to_html = ""
        
        for key, value in self.props.items():
            porps_to_html += f" {key}=\"{value}\""
            
        return porps_to_html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if (not self.value):
            raise ValueError("HTML Error: No value given")
        
        if (not self.tag):
            return self.value
        
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, children=children, props=props)

    def to_html(self):
        if (not self.tag):
            raise ValueError("HTML Error: No tag given")

        if (not self.children):
            raise ValueError("HTML Error: No children given")
        
        html = ""
        for child in self.children:
            html += child.to_html()
        
        return f"<{self.tag}{self.props_to_html()}>{html}</{self.tag}>"
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        s = ""
        
        for key, value in self.props.items():
            s += f"{key}=\"{value}\" "
        
        return s.rstrip(" ")
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag, value, props=props)

    def to_html(self):
        if (not self.value):
            raise ValueError
        
        if (not self.tag):
            return self.value

        if (not self.props):
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        return f"<{self.tag} {self.props_to_html()}>{self.value}</{self.tag}>"
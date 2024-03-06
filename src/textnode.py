class TextNode:
    def __init__(self, text, text_type, url):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, o):
        if not isinstance(o, TextNode):
            return False
        
        return (self.text == o.text and
                self.text_type == o.text_type and
                self.url == o.url)
        
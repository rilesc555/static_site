class TextNode:
    def __init__(self, text, *text_types, url=None):
        self.text = text
        self.text_types = [type for type in text_types]
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_types == other.text_types and self.url == other.url

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_types}, {self.url})"



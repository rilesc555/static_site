text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"

inline_symbols = {
    "**": text_type_bold,
    "*": text_type_italic,
    "`": text_type_code,
}

class TextNode:
    def __init__(self, text, *text_types, url=None, children=None):
        self.text = text
        self.text_types = [type for type in text_types]
        self.url = url
        self.children = children

    def __eq__(self, other):
        return self.text == other.text and self.text_types == other.text_types and self.url == other.url and self.children == other.children

    def __repr__(self):
        pass
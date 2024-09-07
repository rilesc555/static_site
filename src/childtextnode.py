from textnode import *

class ChildTextNode(TextNode):
    def __init__(self, text, *text_types, url=None):
        super().__init__(text, *text_types, url=url, children=None)
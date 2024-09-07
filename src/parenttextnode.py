from textnode import *
from typing import Text


class ParentTextNode(TextNode):
    def __init__(self, *text_types, children=None):
        super().__init__(text=None, *text_types, url=None, children=children)
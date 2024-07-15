import string

from cv2 import randShuffle


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children =  children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        html = ""
        if self.props:
            for key, value in self.props.items():
                html += f" {key}=\"{value}\""
        
        return html
    
    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"

    def __eq__(self, other: object) -> bool:
        return self.tag == other.tag and self.value == other.value and self.children == other.children and self.props == other.props
    

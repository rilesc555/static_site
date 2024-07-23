import string


class HTMLNode:
    def __init__(self, *tags: str, value=None, children=None, props=None) -> None:
        self.tags = [tag for tag in tags] if tags else None
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
        return f"HTMLNode({self.tags}, {self.value}, children: {self.children}, {self.props})"

    def __eq__(self, other: object) -> bool:
        equal_tags = (set(self.tags)==set(other.tags))
        
        return equal_tags and self.value == other.value and self.children == other.children and self.props == other.props
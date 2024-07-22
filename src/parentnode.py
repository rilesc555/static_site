from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, *tags, children, props=None):
        super().__init__(*tags, value=None, children=children, props=props)

    def to_html(self):
        if not self.tags:
            raise ValueError("No tag given")
        if not self.children:
            raise ValueError("No children given")
        else:
            answer = ""
            for tag in self.tags[:-1]:
                answer += f"<{tag}>"
            answer += f"<{self.tags[-1]}{self.props_to_html()}>"
            for node in self.children:
                answer += node.to_html()
            for tag in reversed(self.tags):
                answer += f"</{tag}>"
            return answer

    def __repr__(self):
        return f"ParentNode({self.tags}, children: {self.children}, {self.props})"
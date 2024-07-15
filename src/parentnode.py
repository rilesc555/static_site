from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if not self.tag:
            raise ValueError("No tag given")
        if not self.children:
            raise ValueError("No children given")
        else:
            answer = f"<{self.tag}{self.props_to_html()}>"
            for node in self.children:
                answer += node.to_html()
            answer += f"</{self.tag}>"
            return answer

    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
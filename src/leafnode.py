from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, *tags: str, value, props=None):
        super().__init__(*tags, value=value, children=None, props=props)

    def to_html(self):
        if not self.value:
            raise ValueError
        if not self.tags:
            return self.value
        else:
            answer = ""
            for tag in self.tags[:-1]:
                answer += f"<{tag}>"
            answer += f"<{self.tags[-1]}{self.props_to_html()}>{self.value}"
            for tag in reversed(self.tags):
                answer += f"</{tag}>"
            return answer

    def __repr__(self):
        return f"LeafNode({self.tags}, {self.value}, {self.props})"

# def main():
#     value = "Click me!"
#     tags = ["a", "b"]
#     props = {"href": "https://www.google.com"}
#     testLeaf = LeafNode(*tags, value=value, props=props)
    
#     print(testLeaf.to_html())

# main()
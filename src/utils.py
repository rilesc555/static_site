import leafnode, textnode

def text_node_to_html_node(text_node: textnode.TextNode):
    if text_node.text_type == "text":
        return leafnode.LeafNode(value=text_node.text)
    elif text_node.text_type == "bold":
        return leafnode.LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == "italic":
        return leafnode.LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == "code":
        return leafnode.LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == "link":
        return leafnode.LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    elif text_node.text_type == "image":
        return leafnode.LeafNode(tag="img", value=text_node.text, props={"src": text_node.url, "alt": text_node.alt})
    else:
        raise ValueError("Invalid text type")


def split_nodes_delimiter(old_nodes, delimiter, text_type):

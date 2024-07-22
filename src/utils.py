import string
import types
from leafnode import LeafNode
from textnode import TextNode
from typing import List, Text
import re

def text_node_to_html_node(text_node: TextNode):
    types = []
    props = {}
    for type in text_node.text_types:
        if type == "text":
            continue
        if type == "bold":
            types.append("b")
        elif type == "italic":
            types.append("i")
        elif type == "code":
            types.append("code")
        elif type == "link":
            types.append("a")
            props = {"href": text_node.url}
        elif type == "image":
            types.append("img")
            props = {"src": text_node.url, "alt": text_node.alt}
        else:
            raise ValueError("Invalid text type")
    if props == {}:
        return LeafNode(*types, value=text_node.text)
    else:
        return LeafNode(*types, value=text_node.text, props=props)

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type):
    answer_nodes = []
    for node in old_nodes:
        if delimiter in node.text:
            delim_count = node.text.count(delimiter)
            if delim_count % 2 == 0:
                new_nodes = []
                sections = node.text.split(delimiter)
                for i in range(len(sections)):
                    if i % 2 == 0:
                        new_node = TextNode(sections[i], *node.text_types)
                        new_nodes.append(new_node)
                    else:
                        text_types = node.text_types.copy()
                        text_types.append(text_type)
                        new_node = TextNode(sections[i], *text_types)
                        new_nodes.append(new_node)
                answer_nodes.extend(new_nodes)
            else:
                raise Exception("Invalid markdown syntax: non-matching delimiters")
        else:
            answer_nodes.append(node)
    return answer_nodes    

def extract_markdown_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images

def extract_markdown_links(text):
    links = re.findall(r"\[(.*?)\]\((.*?)\)", text)


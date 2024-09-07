from os import link
import string
import types
from childtextnode import ChildTextNode
from leafnode import LeafNode
from textnode import *
from typing import List, Text
import re

def text_node_to_html_node(text_node: TextNode):
    types = []
    props = {}
    for type in text_node.text_types:
        if type == text_type_text:
            continue
        elif type == text_type_bold:  
            types.append("b")
        elif type == text_type_italic:
            types.append("i")
        elif type == text_type_code:
            types.append("code")
        elif type == text_type_link:
            types.append("a")
            props = {"href": text_node.url}
        elif type == text_type_image:
            types.append("img")
            props = {"src": text_node.url, "alt": text_node.alt}
        else:
            raise ValueError("Invalid text type")
    if props == {}:
        return LeafNode(*types, value=text_node.text)
    else:
        return LeafNode(*types, value=text_node.text, props=props)

def split_nodes_delimiter(old_nodes: List[TextNode], delimiter: str, text_type):
    # answer_nodes = []
    # for node in old_nodes:
    #     if delimiter in node.text:
    #         delim_count = node.text.count(delimiter)
    #         if delim_count % 2 == 0:
    #             new_nodes = []
    #             sections = node.text.split(delimiter)
    #             for i in range(len(sections)):
    #                 if i % 2 == 0:
    #                     new_node = TextNode(sections[i], *node.text_types)
    #                     new_nodes.append(new_node)
    #                 else:
    #                     text_types = node.text_types.copy()
    #                     text_types.append(text_type)
    #                     new_node = TextNode(sections[i], *text_types)
    #                     new_nodes.append(new_node)
    #             answer_nodes.extend(new_nodes)
    #         else:
    #             raise Exception("Invalid markdown syntax: non-matching delimiters")
    #     else:
    #         answer_nodes.append(node)
    # return answer_nodes    
    for node in old_nodes:
        if node is ChildTextNode:


            





def extract_first_image(text):
    image = re.search(r"!\[(.*?)\]\((.*?)\)", text)
    return image.groups() if image else None

def extract_markdown_links(text):
    link = re.search(r"\[(.*?)\]\((.*?)\)", text)
    return link.groups() if link else None


def split_nodes_image(old_nodes: List[TextNode]):
    answer_nodes = []
    for node in old_nodes:
        image = extract_first_image(node.text)
        if not image:
            answer_nodes.append(node)
        else:
            text, link = image[0], image[1]
            delimiter = f"![{text}]({link})"
            sections = node.text.split(delimiter, 1)
            if sections[0]:
                answer_nodes.append(TextNode(sections[0], *node.text_types)) 
            answer_nodes.append(TextNode(text, *node.text_types, text_type_image, url=link))
            if sections[1]:
                answer_nodes.extend(split_nodes_image([TextNode(sections[1], *node.text_types)]))

    return answer_nodes
    
def split_nodes_link(old_nodes: List[TextNode]):
    answer_nodes = []
    for node in old_nodes:
        extracted = extract_markdown_links(node.text)
        if not extracted:
            answer_nodes.append(node)
        else:
            text, link = extracted[0], extracted[1]
            delimiter = f"[{text}]({link})"
            sections = node.text.split(delimiter, 1)
            if sections[0]:
                answer_nodes.append(TextNode(sections[0], *node.text_types)) 
            answer_nodes.append(TextNode(text, *node.text_types, text_type_link, url=link))
            if sections[1]:
                answer_nodes.extend(split_nodes_link([TextNode(sections[1], *node.text_types)]))

    return answer_nodes

def text_to_textnodes(text: str):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    for symbol, text_type in inline_symbols.items():
        nodes = split_nodes_delimiter(nodes, symbol, text_type)

    return nodes

def main():
    text = "This is **text with an *italic* word** and a `code block` and a ![bold obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    nodes = text_to_textnodes(text)
    for node in nodes:
        print(node)

if __name__ == "__main__":
    main()
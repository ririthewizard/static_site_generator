from textnode import *
from htmlnode import *

def main():
    new_node = TextNode("This is a text node", "bold", "https://www.boot.dev")

    print(new_node)

    new_htmlnode = HTMLNode("p", "This is an html node", "", {"href": "https://www.google.com"})

    print(new_htmlnode.props_to_html())


if __name__ == "__main__":
    main()
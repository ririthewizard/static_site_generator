from src.htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: No tag")
        if self.children is None:
            raise ValueError("Be a good parent, give this node's children some love")
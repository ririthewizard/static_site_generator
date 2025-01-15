from htmlnode import HTMLNode
from leafnode import LeafNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: No tag")
        if self.children is None:
            raise ValueError("Be a good parent, give this node's children some love")
        else:
            children_string = ""
            
            if self.child is None:
                children_string += LeafNode(self.tag, self.value, self.props).to_html()
            for child in self.children:
                children_string += child.to_html()
        

node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
)

print(node.to_html())
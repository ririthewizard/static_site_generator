class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    # to be implemented by child classes
    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        for key, value in self.props.items():
            return f" {key}= {value}"

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
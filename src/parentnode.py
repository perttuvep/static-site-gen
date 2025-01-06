from htmlnode import HTMLNode
from leafnode import LeafNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def __repr__(self):
        return f"ParentNode({self.tag} {self.children} {self.props})"

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag required")
        if not self.children:
            raise ValueError("Children required")
        else:
            out = " "
            for c in self.children:
                out += c.to_html()
            if self.props is None:
                return f"<{self.tag}>{out}</{self.tag}>"
            if self.props is not None:
                return f"<{self.tag} {self.props_to_html()}>{out}</{self.tag}>"
            else:
                return out + "This isn't right"

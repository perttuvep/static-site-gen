class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def __eq__(self, other):
        if (
            self.props == other.props
            and self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
        ):
            return True
        else:
            return False

    def __repr__(self):
        return f"HTMLNode({self.tag} {self.value} {self.children} {self.props})"

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        out = ""
        if self.props:
            for k, v in self.props.items():
                out += f' {k} = "{v}"'
        return out

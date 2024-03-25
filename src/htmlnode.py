class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError(
            "Method is not implemented, as it will override by child classes."
        )

    def props_to_html(self):
        if self.props == None:
            return ""
        attributes = ""
        for key, value in self.props.items():
            attributes += f' {key}="{value}"'
        return attributes

    def __repr__(self) -> str:
        return f"HTMLNode(tag: {self.tag}, value: {self.value}, children: {self.children}, props: {self.props})"


class LeafNode(HTMLNode):

    def __init__(self, tag=None, value=None, props=None) -> None:
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError("All leaf nodes require a value")
        elif self.tag == None:
            return self.value
        else:
            html_props = self.props_to_html()
            return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"
        
    def __repr(self): 
        return f"LeafNode(tag: {self.tag}, value: {self.value}, children: {self.children})"


class ParentNode(HTMLNode):

    def __init__(self, tag, children, props=None) -> None:
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Tag is not provided.")
        elif self.children == None:
            raise ValueError("No children of the html tag")
        else:
            child_nodes = ""
            for child in self.children:
                child_nodes += child.to_html()
            return f"<{self.tag}{self.props_to_html()}>{child_nodes}</{self.tag}>"
        
    def __repr(self): 
         return f"ParentNode(tag: {self.tag}, children: {self.children}, props: {self.props})"

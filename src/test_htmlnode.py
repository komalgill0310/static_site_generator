import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):

    def test_props_to_html(self):
        html_node = HTMLNode(
            tag="a",
            value="Click here",
            props={"href": "https://www.boot.dev", "target": "_blank"},
        )
        self.assertEqual(
            html_node.props_to_html(), ' href="https://www.boot.dev" target="_blank"'
        )

    def test_leafnode_to_html_with_no_attributes(self):
        leaf_node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(leaf_node.to_html(), "<p>This is a paragraph of text.</p>")

    def test_leafnode_to_html_with_attributes(self):
        leaf_node_with_props = LeafNode(
            "a", "Click me!", {"href": "https://www.google.com"}
        )
        self.assertEqual(
            leaf_node_with_props.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leafnode_to_html_no_tag(self):
        leaf_node_no_tag = LeafNode(value="I am only raw text")
        self.assertEqual(leaf_node_no_tag.to_html(), "I am only raw text")

    def test_parentnode_to_html_with_children(self):
        parent_node_with_children = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            parent_node_with_children.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_parentnode_to_html_with_props(self):
        parent_node_with_props = ParentNode(
            "ul",
            [
                LeafNode("li", "First"),
                LeafNode("li", "Second"),
                LeafNode("li", "Third"),
            ],
            {"class": "unorder-class-list"},
        )
        self.assertEqual(
            parent_node_with_props.to_html(),
            '<ul class="unorder-class-list"><li>First</li><li>Second</li><li>Third</li></ul>',
        )

    def test_parentnode_to_html_with_nested_elements(self):
        parent_node_with_nested_elements = ParentNode(
            "ol",
            [
                LeafNode("li", "First order list", {"class": "first-order-list"}),
                ParentNode(
                    "ul",
                    [
                        LeafNode(
                            "li",
                            "First Unorder list item",
                            {"class": "first-unorder-list"},
                        )
                    ],
                    {"class": "unorder-list"},
                ),
            ],
            {"class": "order-list"},
        )
        self.assertEqual(
            parent_node_with_nested_elements.to_html(),
            '<ol class="order-list"><li class="first-order-list">First order list</li><ul class="unorder-list"><li class="first-unorder-list">First Unorder list item</li></ul></ol>',
        )

if __name__ == "__main__":
    unittest.main()

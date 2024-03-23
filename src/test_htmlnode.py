import unittest
from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase): 
  
  def test_props_to_html(self): 
    html_node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.boot.dev", "target": "_blank"})
    self.assertEqual(html_node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

  def test_leafnode_to_html(self): 
    leaf_node = LeafNode("p", "This is a paragraph of text.")
    self.assertEqual(leaf_node.to_html(), "<p>This is a paragraph of text.</p>")

  def test_leafnode_to_html_with_attributes(self): 
    leaf_node_with_props = LeafNode("a", "Click me!", None, {"href": "https://www.google.com"})
    self.assertEqual(leaf_node_with_props.to_html(), '<a href="https://www.google.com">Click me!</a>')

  def test_leafnode_to_html_no_tag(self): 
    leaf_node_no_tag = LeafNode(value="I am only raw text")
    self.assertEqual(leaf_node_no_tag.to_html(), "I am only raw text")

if __name__ == "__main__": 
  unittest.main()
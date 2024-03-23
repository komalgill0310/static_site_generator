import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase): 
  
  def test_props_to_html(self): 
    html_node = HTMLNode(tag="a", value="Click here", props={"href": "https://www.boot.dev", "target": "_blank"})
    self.assertEqual(html_node.props_to_html(), ' href="https://www.boot.dev" target="_blank"')

if __name__ == "__main__": 
  unittest.main()
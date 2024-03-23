import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase): 
  def test_eq(self): 
    node = TextNode("This is a text node", "bold")
    node2 = TextNode("This is a text node", "bold")
    self.assertEqual(node, node2)

  def test_eq_false(self): 
    node = TextNode("this is a text node", "italic")
    node2 = TextNode("THIS IS A TEXT NODE", "BOLD")
    self.assertNotEqual(node, node2)

  def test_eq_false2(self): 
    node = TextNode("This is a text node", "code")
    node2 = TextNode("THis is Text node", "image")
    self.assertNotEqual(node, node2)

  def test_eq_url(self): 
    node = TextNode("this is a text node", "italic", "https://www.boot.dev")
    node2 = TextNode("this is a text node", "italic", "https://www.boot.dev")
    self.assertEqual(node, node2)
  
  def test_repr(self): 
    node = TextNode("This is a text node", "bold", "https://www.boot.dev")
    self.assertEqual("This is a text node, bold, https://www.boot.dev", repr(node))


if __name__ == "__main__": 
  unittest.main()
class HTMLNode: 
  
  def __init__(self, tag=None, value=None, children=None, props=None) -> None:
    self.tag = tag                       
    self.value = value
    self.children = children
    self.props = props 

  def to_html(self): 
    raise NotImplementedError
  
  def props_to_html(self):
    if self.props == None: 
      return ""
    attributes = ""
    for key,value in self.props.items():
      attributes += f' {key}="{value}"'
    return attributes
  
  def __repr__(self) -> str:
    print(f"""
            Tag is: {self.tag}
            Value is: {self.value}
            children: {self.children}
            props: {self.props_to_html()}""")
    
class LeafNode(HTMLNode): 

  def __init__(self, tag=None, value=None, children=None, props=None) -> None:
    super().__init__(tag, value, children, props)

  def to_html(self):
    if self.value == None: 
      raise ValueError("All leaf nodes require a value")
    elif self.tag == None: 
      return self.value
    else: 
      html_props = self.props_to_html()
      return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"
  

  
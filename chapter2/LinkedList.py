

class Node:
  def __init__(self, value=None, next=None):
    self.value = value
    self.next = next

  def __str__(self):
    return str(self.value)

  def printAll(self):
    aux = self
    while aux is not None:
      print aux.value
      aux = aux.next

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def peek(self):
    return self.top.value

  def push(self, value):
    newNode = Node(value)
    if self.top is None:
      self.bottom = newNode
      self.top = newNode
      return
    newNode.next = self.top
    self.top = newNode
    self.length += 1


  def pop(self):
   if self.length == 0:
     return
   self.top = self.top.next 

  

  def printStack(self):
    array = []
    currentNode = self.top
    while currentNode != None:
      array.append(currentNode.value)
      currentNode = currentNode.next
    return array

myStack = Stack()
myStack.push(2)
myStack.push(3)
myStack.push(4)
myStack.push(5)
myStack.pop()



print("peek" ,myStack.peek())
print(myStack.printStack())
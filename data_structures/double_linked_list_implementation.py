class Node:
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None
    

class DoubleLinkedList:
  def __init__(self, value):
    self.head = Node(2)
    self.tail = self.head
    self.length = 1
  
  def append(self, value):
    newNode = Node(value)
    newNode.prev = self.tail
    self.tail.next = newNode
    self.tail = newNode
    self.length += 1

  def prepend(self, value):
    newNode = Node(value)
    newNode.next = self.head
    self.head.prev = newNode
    self.head = newNode
    self.length += 1

  def insert(self, index, value):
    if index == 1:
      self.prepend(value)
      return
    if index > self.length:
      self.append(value)
      return
    newNode = Node(value)
    currentNode = self.traverseToIndex(index-1)
    newNode.prev = currentNode
    newNode.next = currentNode.next
    currentNode.next = newNode
    self.length += 1

  def remove(self, index):
    if index == 1:
      self.head = self.head.next
      self.head.prev =None
      return

    if index >= self.length:
      self.tail = self.tail.prev
      self.tail.next = None
      return
    currentNode = self.traverseToIndex(index-1)

    currentNode.next = currentNode.next.next
    currentNode.next.prev = currentNode
    

  def traverseToIndex(self, index):
    currentNode = self.head
    idx = 1 
    while(idx != index):
      currentNode = currentNode.next
      idx += 1
    return currentNode

  def printList(self):
    array =[]
    currentNode = self.head
    while currentNode != None:
      array.append(currentNode.value)
      currentNode = currentNode.next
    return array

myDoubleLinkedList = DoubleLinkedList(2)
myDoubleLinkedList.append(5)
myDoubleLinkedList.prepend(7)
myDoubleLinkedList.insert(5, 4)
myDoubleLinkedList.remove(4)


print(myDoubleLinkedList.printList())
    
  


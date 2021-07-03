class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:
  def __init__(self, value):
    self.head = Node(2)
    self.tail = self.head
    self.length = 1

  def append(self, value):
    newNode = Node(value)
    self.tail.next = newNode
    self.tail = newNode
    self.length += 1

  def prepend(self, value):
    newNode = Node(value)
    newNode.next = self.head
    self.head = newNode
    self.length += 1
    
  def insert(self,index, value):
    if index == 1:
      self.prepend(value)
      return
    if index >= self.length:
      self.append(value)
      return
    currentNode = self.traverseToIndex(index-1)
    newNode = Node(value)
    newNode.next = currentNode.next
    currentNode.next = newNode
    self.length += 1
  


  def remove(self, index):
    if index == 1:
      self.head = self.head.next
    if  index > self.length:
      return 
    currentNode = self.traverseToIndex(index-1)
    currentNode.next = currentNode.next.next 
    self.length -= 1

  def traverseToIndex(self, index):
    currentNode = self.head
    currentIndex = 1
    while(currentIndex != index):
      currentNode = currentNode.next
      currentIndex += 1
    return currentNode

  def reverse(self):
  
    currentNode = self.head
    while(currentNode != None):
      self.prepend(currentNode.value)
      temp = currentNode
      currentNode = currentNode.next
      temp.next = None
       

  def printList(self):
    array = []
    currentNode =  self.head
    while(currentNode != None):
      array.append(currentNode.value)
      currentNode = currentNode.next
    return(array)
    

  
  

myLinkedList = LinkedList(2)
myLinkedList.append(2)
myLinkedList.prepend(3)
myLinkedList.prepend(1)
myLinkedList.insert(2, 7)
myLinkedList.remove(5)

myLinkedList.reverse()



print(myLinkedList.printList(), myLinkedList.length)
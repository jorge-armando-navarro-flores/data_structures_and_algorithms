class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0
  
  def peek(self):
    return self.first.value

  def enqueue(self, value):
    newNode = Node(value)
    if self.first is None:
      self.first = newNode
      self.last = newNode
      self.length += 1
      return

    self.last.next = newNode
    self.last = newNode
    self.length += 1

  def dequeue(self):
    self.first = self.first.next
    self.length -= 1

  def printQueue(self):
    nodes = []
    currentNode = self.first
    while currentNode != None:
      nodes.append(currentNode.value)
      currentNode = currentNode.next
    return nodes

myQueue = Queue()
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.enqueue(4)
myQueue.enqueue(5)
myQueue.dequeue()
myQueue.dequeue()

print(myQueue.printQueue())
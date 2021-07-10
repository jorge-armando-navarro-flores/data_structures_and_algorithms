from data_structures.binary_search_tree_implementation import myBST
import queue


def breadth_first_search(root):
  currentNode = root
  nodes = []
  myQueue = queue.Queue()
  myQueue.put(currentNode)

  
  while myQueue.qsize() > 0:
    currentNode = myQueue.get()
    nodes.append(currentNode.value)
    if currentNode.left:
      myQueue.put(currentNode.left)
    if currentNode.right:
      myQueue.put(currentNode.right)
  return nodes

print(breadth_first_search(myBST.root))
  

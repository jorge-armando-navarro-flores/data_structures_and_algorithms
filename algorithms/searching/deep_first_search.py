from data_structures.binary_search_tree_implementation import myBST


def deep_first_search(tree, order):
  nodes = []
  if order == "inorder":
    deep_first_search_inorder(tree.root, nodes)
  elif order == "preorder":
    deep_first_search_preorder(tree.root, nodes)
  elif order == "postorder":
    deep_first_search_postorder(tree.root, nodes)
  return nodes

def deep_first_search_inorder(root, nodes = []):
  if root is None:
    return

  if root.left:
    deep_first_search_inorder(root.left, nodes)
  nodes.append(root.value)
  if root.right:
    deep_first_search_inorder(root.right, nodes)

def deep_first_search_preorder(root, nodes = []):
  if root is None:
    return
  nodes.append(root.value)
  if root.left:
    deep_first_search_preorder(root.left, nodes)
  if root.right:
    deep_first_search_preorder(root.right, nodes)

def deep_first_search_postorder(root, nodes = []):
  if root is None:
    return

  if root.left:
    deep_first_search_postorder(root.left, nodes)
  if root.right:
    deep_first_search_postorder(root.right, nodes)
  nodes.append(root.value)
  
print(deep_first_search(myBST, order="inorder"))

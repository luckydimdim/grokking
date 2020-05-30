class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths2(root, sum):
  '''
  Given a binary tree and a number ‘S’,
  find all paths from root-to-leaf
  such that the sum of all the node values of each path equals ‘S’.
  '''
  allPaths = []

  find_paths_recursive(root, sum, [], allPaths)

  return allPaths

def find_paths_recursive(root, sum, current, result):
  if root is None:
    return

  current.append(root.val)

  if sum == root.val and root.left is None and root.right is None:
    result.append(list(current))

  find_paths_recursive(root.left, sum - root.val, current, result)
  find_paths_recursive(root.right, sum - root.val, current, result)

  del current[-1]

def find_paths(root, sum):
  '''
  Given a binary tree and a number ‘S’,
  find all paths from root-to-leaf
  such that the sum of all the node values of each path equals ‘S’.
  '''
  result = []
  do_find_paths(root, sum, 0, [], result)
  return result

def do_find_paths(root, S, sum, current, result):
  if root is None:
    return

  current.append(root.val)

  if root.left is None and root.right is None:
    if root.val + sum == S:
      result.append(list(current))

  do_find_paths(root.left, S, sum + root.val, current, result)
  do_find_paths(root.right, S, sum + root.val, current, result)

  del current[-1]

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()

from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  '''
  Given a binary tree, populate an array to represent its level-by-level traversal
  in reverse order, i.e., the lowest level comes first.
  You should populate the values of all nodes in each level
  from left to right in separate sub-arrays.
  '''
  result = deque()

  if root is None:
    return result

  queue = deque()
  queue.append(root)

  while queue:
    level_size = len(queue)
    level = []

    for _ in range(level_size):
      curr = queue.popleft()
      level.append(curr.val)

      if curr.left:
        queue.append(curr.left)

      if curr.right:
        queue.append(curr.right)

    result.appendleft(level)

  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()

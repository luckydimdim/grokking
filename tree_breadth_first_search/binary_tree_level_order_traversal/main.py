from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse2(root):
  '''
  Given a binary tree, populate an array to represent its level-by-level traversal.
  You should populate the values of all nodes of each level from left to right in separate sub-arrays.
  '''
  result = []

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

      if curr.left is not None:
        queue.append(curr.left)

      if curr.right is not None:
        queue.append(curr.right)

    result.append(level)

  return result

def traverse(root):
  '''
  Given a binary tree, populate an array to represent its level-by-level traversal.
  You should populate the values of all nodes of each level from left to right in separate sub-arrays.
  '''
  result = []

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

    result.append(level)

  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))


main()

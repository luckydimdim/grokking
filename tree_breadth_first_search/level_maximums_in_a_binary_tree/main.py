from collections import deque
import math

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_level_averages(root):
  '''
  Given a binary tree, populate an array to represent the maximums of all of its levels.
  '''
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)

  while queue:
    level_size = len(queue)
    level_max = -math.inf

    for _ in range(level_size):
      curr = queue.popleft()

      level_max = max(curr.val, level_max)

      if curr.left:
        queue.append(curr.left)

      if curr.right:
        queue.append(curr.right)

    result.append(level_max)

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()








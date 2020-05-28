from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_right_view2(root):
  '''
  Given a binary tree, return an array containing nodes in its right view.
  The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
  '''
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)
  result.append(root)

  while queue:
    level_size = len(queue)
    last_on_level = None

    for _ in range(level_size):
      curr = queue.popleft()

      if curr.left:
        queue.append(curr.left)
        last_on_level = curr.left

      if curr.right:
        queue.append(curr.right)
        last_on_level = curr.right

    if last_on_level:
      result.append(last_on_level)

  return result

def tree_right_view(root):
  '''
  Given a binary tree, return an array containing nodes in its right view.
  The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.
  '''
  result = []
  if root is None:
    return result

  queue = deque()
  queue.append(root)

  while queue:
    level_size = len(queue)

    for i in range(level_size):
      curr = queue.popleft()

      if curr.left:
        queue.append(curr.left)

      if curr.right:
        queue.append(curr.right)

      if i == level_size - 1:
        result.append(curr)

  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()


from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  '''
  Given a binary tree and a node, find the level order successor of the given node in the tree.
  The level order successor is the node that appears right after the given node in the level order traversal.
  '''
  if root is None:
    return None

  queue = deque()
  queue.append(root)

  while queue:
    curr = queue.popleft()

    if curr.left:
      queue.append(curr.left)

    if curr.right:
      queue.append(curr.right)

    if key == curr.val:
      break

  if queue is None:
    return None

  return queue[0]


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()

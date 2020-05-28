from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  '''
  Given a binary tree, populate an array to represent its zigzag level order traversal.
  You should populate the values of all nodes of the first level from left to right,
  then right to left for the next level and keep alternating in the same manner for the following levels.
  '''
  result = []

  if root is None:
    return result

  queue = deque()
  queue.append(root)

  zigzag = True

  while queue:
    level_size = len(queue)
    level = deque()

    zigzag = not zigzag

    for _ in range(level_size):
      curr = queue.popleft()

      if zigzag == True:
        level.appendleft(curr.val)
      else:
        level.append(curr.val)

      if curr.left:
        queue.append(curr.left)

      if curr.right:
        queue.append(curr.right)

    result.append(list(level))

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()

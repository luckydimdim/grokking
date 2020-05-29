class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root):
  '''
  Given a binary tree, find the root-to-leaf path with the maximum sum.
  '''
  result = []

  find_path_recursive(root, [], result)

  return result

def find_path_recursive(root, current, result):
  if root is None:
    return

  current.append(root.val)

  if root.left is None and root.right is None:
    current_maximum = sum(current)
    absolute_maximum = sum(result)

    if current_maximum > absolute_maximum:
      while len(result) > 0:
        del result[-1]

      for i in range(len(current)):
        result.append(current[i])

  if root.left is not None:
    find_path_recursive(root.left, current, result)

  if root.right is not None:
    find_path_recursive(root.right, current, result)

  del current[-1]

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree paths " +
        ": " + str(find_paths(root)))

main()

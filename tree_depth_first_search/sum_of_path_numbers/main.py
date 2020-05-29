class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_sum_of_path_numbers(root, path_sum = 0):
  '''
  Given a binary tree where each node can only have a digit (0-9) value,
  each root-to-leaf path will represent a number.
  Find the total sum of all the numbers represented by all paths.
  '''
  if root is None:
    return 0

  path_sum = path_sum * 10 + root.val

  if root.left is None and root.right is None:
    return path_sum

  return find_sum_of_path_numbers(root.left, path_sum) + find_sum_of_path_numbers(root.right, path_sum)

def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()

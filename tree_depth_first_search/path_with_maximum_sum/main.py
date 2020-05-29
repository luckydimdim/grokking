import math


class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

class MaxPathSum:
  def find_maximum_path_sum(self, root):
    '''
    Find the path with the maximum sum in a given binary tree.
    Write a function that returns the maximum sum.
    A path can be defined as a sequence of nodes between any two nodes
    and doesn’t necessarily pass through the root.
    '''
    self.max_sum = -math.inf
    self.calculate_max_sum(root)
    return self.max_sum


  def calculate_max_sum(self, root):
    if root is None:
      return 0

    left = max(self.calculate_max_sum(root.left), 0)
    right = max(self.calculate_max_sum(root.right), 0)

    curr_sum = left + right + root.val
    self.max_sum = max(self.max_sum, curr_sum)

    return max(left, right) + root.val

def main():
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  max_path_sum = MaxPathSum()
  print("Maximum Path Sum: " + str(max_path_sum.find_maximum_path_sum(root)))
  root.left.left = TreeNode(1)
  root.left.right = TreeNode(3)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  print("Maximum Path Sum: " + str(max_path_sum.find_maximum_path_sum(root)))

  root = TreeNode(-1)
  root.left = TreeNode(-3)
  print("Maximum Path Sum: " + str(max_path_sum.find_maximum_path_sum(root)))


main()

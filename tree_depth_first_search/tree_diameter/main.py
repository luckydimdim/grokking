class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


class TreeDiameter:

  def __init__(self):
    self.tree_diameter = 0

  def find_diameter2(self, root):
    '''
    Given a binary tree, find the length of its diameter.
    The diameter of a tree is the number of nodes on the longest path
    between any two leaf nodes. The diameter of a tree may or may not pass through the root.
    Note: You can always assume that there are at least two leaf nodes in the given tree.
    '''
    self.calculate_height(root)
    return self.tree_diameter

  def calculate_height(self, root):
    if root is None:
      return 0

    left_height = self.calculate_height(root.left)
    right_height = self.calculate_height(root.right)

    height = left_height + right_height + 1
    self.tree_diameter = max(self.tree_diameter, height)

    return max(left_height, right_height) + 1


  def find_diameter(self, root):
    '''
    Given a binary tree, find the length of its diameter.
    The diameter of a tree is the number of nodes on the longest path
    between any two leaf nodes. The diameter of a tree may or may not pass through the root.
    Note: You can always assume that there are at least two leaf nodes in the given tree.
    '''
    self.calculate_depth(root)
    return self.tree_diameter

  def calculate_depth(self, root):
    if root is None:
      return 0

    left = self.calculate_depth(root.left)
    right = self.calculate_depth(root.right)

    sum = left + right + 1
    self.tree_diameter = max(self.tree_diameter, sum)

    return max(left, right) + 1

def main():
  treeDiameter = TreeDiameter()
  root = TreeNode(1)
  root.left = TreeNode(2)
  root.right = TreeNode(3)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(5)
  root.right.right = TreeNode(6)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))
  root.left.left = None
  root.right.left.left = TreeNode(7)
  root.right.left.right = TreeNode(8)
  root.right.right.left = TreeNode(9)
  root.right.left.right.left = TreeNode(10)
  root.right.right.left.left = TreeNode(11)
  print("Tree Diameter: " + str(treeDiameter.find_diameter(root)))


main()








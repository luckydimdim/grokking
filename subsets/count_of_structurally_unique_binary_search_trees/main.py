class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None


def count_trees(n):
  '''
  Given a number ‘n’, write a function to
  return the count of structurally unique Binary Search Trees (BST)
  that can store values 1 to ‘n’.
  '''
  if n <= 1:
    return 1

  count = 0
  for i in range(1, n+1):
    # making 'i' root of the tree
    count_of_left_subtrees = count_trees(i - 1)
    count_of_right_subtrees = count_trees(n - i)
    count += (count_of_left_subtrees * count_of_right_subtrees)

  return count


def main():
  print("Total trees: " + str(count_trees(2)))
  print("Total trees: " + str(count_trees(3)))


main()







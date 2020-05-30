class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def count_paths2(root, S):
  '''
  Given a binary tree and a number ‘S’, find all paths in the tree
  such that the sum of all the node values of each path equals ‘S’.
  Please note that the paths can start or end at any node
  but all paths must follow direction from parent to child (top to bottom).
  '''

  return count_paths_recursive(root, S, [])

def count_paths_recursive(root, S, curr):
  counter = 0
  if root is None:
    return counter

  curr.append(root.val)

  curr_sum = 0
  for i in range(len(curr)-1, -1, -1):
    curr_sum += curr[i]
    if curr_sum == S:
      counter += 1

  counter += count_paths_recursive(root.left, S, curr)
  counter += count_paths_recursive(root.right, S, curr)
  del curr[-1]

  return counter







def count_paths(root, S):
  '''
  Given a binary tree and a number ‘S’, find all paths in the tree
  such that the sum of all the node values of each path equals ‘S’.
  Please note that the paths can start or end at any node
  but all paths must follow direction from parent to child (top to bottom).
  '''

  return do_count_paths(root, S, [])

def do_count_paths(root, S, curr):
  counter = 0
  if root is None:
    return counter

  curr.append(root)

  sum = 0
  for i in range(len(curr)-1, -1, -1):
    sum += curr[i].val
    if sum == S:
      counter += 1

  counter += do_count_paths(root.left, S, curr)
  counter += do_count_paths(root.right, S, curr)

  del curr[-1]

  return counter










def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has paths: " + str(count_paths(root, 11)))


main()

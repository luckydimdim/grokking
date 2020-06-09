class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_unique_trees(n):
    '''
    Given a number ‘n’, write a function to
    return all structurally unique Binary Search Trees (BST)
    that can store values 1 to ‘n’?
    '''
    if n <= 0:
        return []

    return find_unique_trees_recursive(1, n)

def find_unique_trees_recursive(start, end):
    result = []
    # base condition, return 'None' for an empty sub-tree
    # consider n = 1, in this case we will have start = end = 1, this means we should have only one tree
    # we will have two recursive calls, findUniqueTreesRecursive(1, 0) & (2, 1)
    # both of these should return 'None' for the left and the right child
    if start > end:
        result.append(None)
        return result

    for i in range(start, end + 1):
        left_tree = find_unique_trees_recursive(start, i - 1)
        right_tree = find_unique_trees_recursive(i + 1, end)

        for left in left_tree:
            for right in right_tree:
                root = TreeNode(i)
                root.left = left
                root.right = right

                result.append(root)

    return result

def main():
    #print("Total trees: " + str(len(find_unique_trees(1))))
    print("Total trees: " + str(len(find_unique_trees(2))))
    print("Total trees: " + str(len(find_unique_trees(3))))


main()

def find_subsets2(nums):
    '''
    Given a set with distinct elements, find all of its distinct subsets.
    '''
    subsets = [[]]
    for n in range(len(nums)):
        l = len(subsets)
        for s in range(l):
            subsets.append(subsets[s] + [nums[n]])

    return subsets

def find_subsets(nums):
    '''
    Given a set with distinct elements,
    find all of its distinct subsets.
    '''
    result = [[]]
    for num in range(len(nums)):
        queue_size = len(result)
        for i in range(queue_size):
            curr = result[i]
            result.append(curr + [nums[num]])
    return result

def main():

    print("Here is the list of subsets: " + str(find_subsets([1, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3])))


main()

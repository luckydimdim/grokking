def find_subsets2(nums):
    '''
    Given a set of numbers that might contain duplicates, find all of its distinct subsets.
    '''
    subsets = [[]]
    nums.sort()

    for n in range(len(nums)):
        start = 0
        length = len(subsets)

        if n > 0 and nums[n - 1] == nums[n]:
            start = finish + 1

        finish = len(subsets) - 1

        for s in range(start, finish + 1):
            subsets.append(subsets[s] + [nums[n]])

    return subsets

def find_subsets(nums):
    '''
    Given a set of numbers that might contain duplicates,
    find all of its distinct subsets.
    '''
    nums.sort()
    result = [[]]
    for num in range(len(nums)):
        if num > 0 and nums[num] == nums[num - 1]:
            start = end + 1
        else:
            start = 0

        end = len(result)

        for i in range(start, end):
            result.append(result[i] + [nums[num]])
    return result


def main():
    print("Here is the list of subsets: " + str(find_subsets([1, 3, 3])))
    print("Here is the list of subsets: " + str(find_subsets([1, 5, 3, 3])))


main()

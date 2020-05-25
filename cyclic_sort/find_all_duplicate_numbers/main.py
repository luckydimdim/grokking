def find_all_duplicates(nums):
    '''
    We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
    The array has some duplicates, find all the duplicate numbers without using any extra space.
    '''
    result = []
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            result.append(nums[i])

    return result

nums = [3, 4, 4, 5, 5]

print(find_all_duplicates(nums))
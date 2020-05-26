def find_first_missing_positive(nums):
    '''
    Given an unsorted array containing numbers,
    find the smallest missing positive number in it.
    '''
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] >= 0 and nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return len(nums) + 1

nums = [3, 2, 5, 1]

print(find_first_missing_positive(nums))
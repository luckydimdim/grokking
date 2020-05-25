def find_missing_number(nums):
    '''
    We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
    Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.
    '''
    i, n = 0, len(nums)
    while i < n:
        j = nums[i]
        if nums[i] != i and nums[i] < n:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if i != nums[i]:
            return i

    return n

nums = [8, 3, 5, 2, 4, 6, 0, 1]

print(find_missing_number(nums))

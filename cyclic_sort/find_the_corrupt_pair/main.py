def find_corrupt_numbers(nums):
    '''
    We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’.
    The array originally contained all the numbers from 1 to ‘n’, but due to a data error,
    one of the numbers got duplicated which also resulted in one number going missing.
    Find both these numbers.
    '''
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    for i in range(n):
        if nums[i] != i + 1:
            return [nums[i], i + 1]

    return [-1, -1]

nums = [3, 1, 2, 3, 6, 4]

print(find_corrupt_numbers(nums))
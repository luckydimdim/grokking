def find_duplicate2(nums):
    '''
    We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
    The array has only one duplicate but it can be repeated multiple times.
    Find that duplicate number without using any extra space.
    You are, however, allowed to modify the input array.
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
            return nums[i]

    return -1

def find_duplicate(nums):
    '''
    We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
    The array has only one duplicate but it can be repeated multiple times.
    Find that duplicate number without using any extra space.
    You are, however, allowed to modify the input array.
    '''
    i, n = 0, len(nums)

    while i < n:
        if nums[i] != i + 1:
            j = nums[i] - 1

            if nums[i] == nums[j]:
                return nums[j]

            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    return -1

nums = [2, 4, 1, 4, 4]

print(find_duplicate(nums))
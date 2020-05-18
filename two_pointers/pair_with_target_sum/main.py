def pair_with_targetsum2(array, target_sum):
    '''
    Given an array of sorted numbers and a target sum,
    find a pair in the array whose sum is equal to the given target.
    Write a function to return the indices of the two numbers
    (i.e. the pair) such that they add up to the given target.
    '''
    left = 0
    right = len(array) - 1

    while left < right:
        current_sum = array[left] + array[right]

        if current_sum == target_sum:
            return [left, right]
        elif current_sum > target_sum:
            right -= 1
        else:
            left += 1

    return [-1, -1]

def pair_with_targetsum(array, target_sum):
    '''
    Given an array of sorted numbers and a target sum,
    find a pair in the array whose sum is equal to the given target.
    Write a function to return the indices of the two numbers
    (i.e. the pair) such that they add up to the given target.
    '''
    nums = {}

    for i in range(len(array)):
        if array[i] not in nums:
            nums[target_sum - array[i]] = i
            continue

        return [nums[array[i]], i]

    return [-1, -1]

array = [1, 2, 3, 4, 6]
k = 6

print(pair_with_targetsum2(array, k))
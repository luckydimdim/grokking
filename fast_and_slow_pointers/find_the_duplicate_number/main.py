def find_duplicate(nums):
    '''
    We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’.
    The array has only one duplicate but it can be repeated multiple times.
    Find that duplicate number without using any extra space.
    You are, however, allowed to modify the input array.
    '''
    slow, fast = nums[0], nums[nums[0]]

    while fast != slow:
        slow = nums[slow]
        fast = nums[nums[fast]]

    current = slow
    cycle_length = 1

    while current != nums[slow]:
        current = nums[current]
        cycle_length += 1

    slow, fast = nums[0], nums[0]

    while cycle_length > 0:
        fast = nums[fast]
        cycle_length -= 1

    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

nums = [2, 1, 3, 5, 4, 3]

print(find_duplicate(nums))
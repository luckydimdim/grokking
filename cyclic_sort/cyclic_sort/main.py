def cyclic_sort(nums):
    '''
    We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number
    from 1 to ‘n’ based on their creation sequence. This means that the object with sequence number ‘3’
    was created just before the object with sequence number ‘4’.

    Write a function to sort the objects in-place on their creation sequence number in O(n)
    and without any extra space. For simplicity, let’s assume we are passed an integer array
    containing only the sequence numbers, though each number is actually an object.
    '''
    i = 0
    while i < len(nums):
        j = nums[i] - 1

        if nums[i] == i + 1:
            i += 1
        else:
            nums[i], nums[j] = nums[j], nums[i]

    return nums

nums = [3, 1, 5, 4, 2]

print(cyclic_sort(nums))
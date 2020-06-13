def can_partition2(nums):
    '''
    Given a set of positive numbers,
    find if we can partition it into two subsets such that
    the sum of elements in both subsets is equal.
    '''
    s = sum(nums)
    if s % 2 != 0:
        return False

    dp = [[-1 for x in range(s + 1)] for y in range(len(nums))]

    return can_partition_recursive(nums, s // 2, 0)

def can_partition_recursive(nums, amount, index):
    if amount == 0:
        return True

    if index >= len(nums):
        return False

    case1 = 0
    if nums[index] <= amount:
        case1 = can_partition_recursive(nums, amount - nums[index], index + 1)
    case2 = can_partition_recursive(nums, amount, index + 1)

    return case1 or case2

def can_partition(nums):
    l = len(nums)
    s = sum(nums)

    if s % 2 != 0:
        return False

    hs = s // 2
    result = [[False for x in range(hs+1)] for y in range(l)]

    for i in range(l):
        result[i][0] = True

    for i in range(hs+1):
        result[0][i] = True

    for n in range(1, l):
        for h in range(1, hs+1):
            if result[n - 1][h]:
                result[n][h] = True
            elif nums[n] <= h:
                result[n][h] = result[n - 1][h - nums[n]]

    return result[l - 1][hs]



def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 4])))
    print("Can partition: " + str(can_partition([1, 1, 3, 4, 7])))
    print("Can partition: " + str(can_partition([2, 3, 4, 6])))

main()

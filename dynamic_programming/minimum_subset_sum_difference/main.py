def can_partition2(num):
    '''
    Given a set of positive numbers,
    partition the set into two subsets
    with minimum difference between their subset sums.
    '''
    dp = [[-1 for x in range(sum(num) + 1)] for y in range(len(num))]
    return can_partition_recursive2(dp, num, left = 0, right = 0, index = 0)

def can_partition_recursive2(dp, num, left, right, index):
    if index == len(num):
        return abs(left - right)

    if dp[index][left] == -1:
        first = can_partition_recursive2(dp, num, left + num[index], right, index + 1)
        second = can_partition_recursive2(dp, num, left, right + num[index], index + 1)

        dp[index][left] = min(first, second)

    return dp[index][left]

def can_partition3(num):
    '''
    Given a set of positive numbers,
    partition the set into two subsets
    with minimum difference between their subset sums.
    '''
    s = sum(num)
    n = len(num)
    dp = [[False for x in range(s // 2 + 1)] for y in range(n)]

    for i in range(n):
        dp[i][0] = True

    for j in range(0, s // 2 + 1):
        if j >= num[0]:
            dp[0][j] = num[0] == j

    for i in range(1, n):
        for j in range(1, s // 2 + 1):
            if dp[i - 1][j]:
                dp[i][j] = dp[i - 1][j]
            elif j >= num[i]:
                dp[i][j] = dp[i - 1][j - num[i]]

    sum1 = 0
    for i in range(s // 2, -1, -1):
        if dp[n - 1][i]:
            sum1 = i
            break

    sum2 = s - sum1
    return abs(sum2 - sum1)

def can_partition4(num):
    return can_partition_recursive(num, 0, 0, 0)

def can_partition_recursive(num, index, first, second):
    if index == len(num):
        return abs(first - second)

    left = can_partition_recursive(num, index + 1, first + num[index], second)
    right = can_partition_recursive(num, index + 1, first, second + num[index])

    return min(left, right)

def can_partition(nums):
    s = sum(nums) // 2 + 1
    l = len(nums)
    dp = [[False for x in range(s)] for y in range(l)]

    for i in range(1, s):
        dp[0][i] = nums[0] == i

    for j in range(l):
        dp[j][0] = True

    for i in range(1, l):
        for j in range(1, s):
            if dp[i - 1][j]:
                dp[i][j] = True
            elif j >= nums[i]:
                dp[i][j] = dp[i - 1][j - nums[i]]

    i = l - 1
    j = s - 1
    while dp[i][j] == False:
        j -= 1

    sum1 = j
    sum2 = sum(nums) - sum1

    return abs(sum1 - sum2)

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 9])))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5])))
    print("Can partition: " + str(can_partition([1, 3, 100, 4])))

main()



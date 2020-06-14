def find_target_subsets2(num, s):
    '''
    You are given a set of positive numbers and a target sum ‘S’.
    Each number should be assigned either a ‘+’ or ‘-’ sign.
    We need to find the total ways to assign symbols to
    make the sum of the numbers equal to the target ‘S’.
    '''
    # left - right = s
    # left + right = sum(num)
    # left - right + left + right = s + sum(num)
    # 2 * left = s + sum(num)
    # left = (s + sum(num)) / 2
    return find_target_subsets_recursive(num, (s + sum(num)) / 2, 0)

def find_target_subsets_recursive(nums, total, index):
    if total == 0:
        return 1

    if index == len(nums):
        return 0

    result = 0

    if total >= nums[index]:
        result += find_target_subsets_recursive(nums, total - nums[index], index+1)

    result += find_target_subsets_recursive(nums, total, index+1)

    return result

def find_target_subsets3(nums, s):
    nums_len = len(nums)
    total = (s + sum(nums)) // 2 + 1

    if sum(nums) < s or (s + sum(nums)) % 2 == 1:
        return 0

    dp = [[0 for x in range(total)] for y in range(nums_len)]

    for i in range(nums_len):
        dp[i][0] = 1

    for i in range(1, total):
        if i == nums[0]:
            dp[0][i] = 1

    for i in range(1, nums_len):
        for j in range(1, total):
            dp[i][j] = dp[i - 1][j]

            if j >= nums[i]:
                dp[i][j] += dp[i - 1][j - nums[i]]

    return dp[nums_len - 1][total - 1]

def find_target_subsets(nums, s):
    nums_len = len(nums)
    total = (s + sum(nums)) // 2 + 1

    if sum(nums) < s or (s + sum(nums)) % 2 == 1:
        return 0

    dp = [0 for x in range(total)]
    dp[0] = 1

    for i in range(1, total):
        if i == nums[0]:
            dp[i] = 1

    for i in range(1, nums_len):
        for j in range(total - 1, -1, -1):
            if j >= nums[i]:
                dp[j] += dp[j - nums[i]]

    return dp[total - 1]

def main():
    print("Total ways: " + str(find_target_subsets([1, 1, 2, 3], 1)))
    print("Total ways: " + str(find_target_subsets([1, 2, 7, 1], 9)))

main()
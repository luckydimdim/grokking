def count_subsets2(num, sum):
    '''
    Given a set of positive numbers,
    find the total number of subsets whose
    sum is equal to a given number ‘S’.
    '''
    return count_subsets_recursive2(num, sum, 0)

def count_subsets_recursive2(num, sum, index):
    if sum == 0:
        return 1

    if index == len(num):
        return 0

    total = 0
    if sum >= num[index]:
        total += count_subsets_recursive2(num, sum - num[index], index + 1)

    total += count_subsets_recursive2(num, sum, index + 1)

    return total

def count_subsets3(num, sum):
    dp = [[-1 for x in range(sum + 1)] for y in range(len(num))]
    return count_subsets_recursive(dp, num, sum, 0)

def count_subsets_recursive(dp, num, sum, index):
    if sum == 0:
        return 1

    if index == len(num):
        return 0

    total = 0

    if sum >= num[index]:
        if dp[index][sum - num[index]] == -1:
            dp[index][sum - num[index]] = count_subsets_recursive(dp, num, sum - num[index], index + 1)
        total += dp[index][sum - num[index]]

    if dp[index][sum] == -1:
        dp[index][sum] = count_subsets_recursive(dp, num, sum, index + 1)

    total += dp[index][sum]

    return total

def count_subsets4(num, sum):
    dp = [[0 for x in range(sum + 1)] for y in range(len(num))]

    for i in range(len(num)):
        dp[i][0] = 1

    for i in range(sum + 1):
        if i == num[0]:
            dp[0][i] = 1

    for i in range(len(num)):
        for j in range(sum + 1):
            dp[i][j] = dp[i - 1][j]

            if j >= num[i]:
                dp[i][j] += dp[i - 1][j - num[i]]

    return dp[len(num) - 1][sum]

def count_subsets(num, sum):
    dp = [0 for x in range(sum + 1)]

    dp[0] = 1

    for i in range(1, sum + 1):
        dp[i] = 1 if i == num[0] else 0

    for i in range(1, len(num)):
        for j in range(sum, -1, -1):
            if j >= num[i]:
                dp[j] += dp[j - num[i]]

    return dp[sum]

def main():
    print("Total number of subsets " + str(count_subsets([1, 1, 2, 3], 4)))
    print("Total number of subsets: " + str(count_subsets([1, 2, 7, 1, 5], 9)))

main()


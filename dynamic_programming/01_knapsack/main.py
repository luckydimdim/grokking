def solve_knapsack2(profits, weights, capacity):
  memo = [[-1 for x in range(capacity+1)] for y in range(len(profits))]
  return knapsack_recursive(memo, profits, weights, capacity, 0)

def knapsack_recursive(memo, profits, weights, capacity, index):
  if index >= len(profits) or capacity <= 0:
    return 0

  if memo[index][capacity] != -1:
    return memo[index][capacity]

  left_profit, right_profit = 0, 0
  if weights[index] <= capacity:
    left_profit = profits[index] + knapsack_recursive(memo, profits, weights, capacity - weights[index], index+1)

  right_profit = knapsack_recursive(memo, profits, weights, capacity, index+1)

  max_profit = max(left_profit, right_profit)

  if memo[index][capacity] == -1:
    memo[index][capacity] = max_profit

  return max_profit

def solve_knapsack3(profits, weights, capacity):
  n = len(profits)

  if capacity <= 0 or n == 0 or len(weights) != n:
    return 0

  dp = [[0 for x in range(capacity+1)] for y in range(2)]

  for c in range(capacity+1):
    if weights[0] <= c:
      dp[0][c] = dp[1][c] = profits[0]

  for i in range(1, n):
    for c in range(1, capacity+1):
      profit1, profit2 = 0, 0
      if weights[i] <= c:
        profit1 = profits[i] + dp[(i - 1) % 2][c - weights[i]]

      profit2 = dp[(i - 1) % 2][c]
      dp[i % 2][c] = max(profit1, profit2)

  print_selected_elements(dp, weights, profits, capacity)

  return dp[(n - 1) % 2][capacity]

def print_selected_elements(dp, weights, profits, capacity):
  result = []
  n = len(weights)
  total = dp[(n - 1) % 2][capacity]
  for i in range(n-1, 0, -1):
    if total != dp[(i - 1) % 2][capacity]:
      result.append(weights[i])
      capacity -= weights[i]
      total -= profits[i]

  if total != 0:
    result.append(weights[0])

  print(result)

def solve_knapsack4(profits, weights, capacity):
  n = len(profits)

  if capacity <= 0 or n == 0 or len(weights) != n:
    return 0

  dp = [0 for x in range(capacity+1)]

  for c in range(capacity+1):
    if weights[0] <= c:
      dp[c] = profits[0]

  for i in range(1, n):
    for c in range(capacity, -1, -1):
      profit1, profit2 = 0, 0
      if weights[i] <= c:
        profit1 = profits[i] + dp[c - weights[i]]

      profit2 = dp[c]
      dp[c] = max(profit1, profit2)

  return dp[capacity]

def solve_knapsack5(profits, weights, capacity):
  dp = [[-1 for x in range(capacity+1)] for y in range(len(weights))]
  return solve_knapsack_rec(dp, profits, weights, capacity, 0)

def solve_knapsack_rec(dp, profits, weights, capacity, index):
  if index >= len(weights) or capacity <= 0:
    return 0

  if dp[index][capacity] != -1:
    return dp[index][capacity]

  left = 0
  if weights[index] <= capacity:
    left = profits[index] + solve_knapsack_rec(dp, profits, weights, capacity-weights[index], index+1)

  right = solve_knapsack_rec(dp, profits, weights, capacity, index+1)

  if dp[index][capacity] == -1:
    dp[index][capacity] = max(left, right)

  return dp[index][capacity]

def solve_knapsack(profits, weights, capacity):
  dp = [[0 for x in range(capacity+1)] for y in range(2)]

  for c in range(capacity+1):
    if weights[0] <= c:
      dp[0][c] = profits[0]

  for i in range(1, len(profits)):
    for c in range(0, capacity+1):
      first = 0
      if weights[i] <= c:
        first = profits[i] + dp[(i - 1) % 2][c - weights[i]]
      second = dp[(i - 1) % 2][c]
      dp[i % 2][c] = max(first, second)

  return dp[(len(profits) - 1) % 2][capacity]

def main():
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 5))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 6))
  print(solve_knapsack([1, 6, 10, 16], [1, 2, 3, 5], 7))

main()
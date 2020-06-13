def can_partition2(num, sum):
    '''
    Given a set of positive numbers,
    determine if a subset exists whose
    sum is equal to a given number ‘S’.
    '''
    start, total = 0, 0
    for end in range(len(num)):
      total += num[end]

      while total > sum:
        total -= num[start]
        start += 1

      if total == sum:
        return True

    return False

def can_partition3(num, sum):
  return can_partition_recursive(num, sum, 0)

def can_partition_recursive(num, sum, index):
  if index == len(num):
    return False

  if sum == 0:
    return True

  first = 0
  if num[index] <= sum:
    first = can_partition_recursive(num, sum - num[index], index+1)
  second = can_partition_recursive(num, sum, index+1)

  return first or second

def can_partition2(nums, sum):
  result = [[False for x in range(sum+1)] for y in range(len(nums))]

  for i in range(len(nums)):
    result[i][0] = True

  for i in range(1, sum+1):
    if i == nums[0]:
      result[0][i] = True

  for i in range(1, len(nums)):
    for j in range(1, sum+1):
      if result[i - 1][j]:
        result[i][j] = True
      elif nums[i] <= j:
        result[i][j] = result[i - 1][j - nums[i]]

  return result[len(nums) - 1][sum]

def can_partition(nums, sum):
  result = [False for x in range(sum+1)]

  for i in range(1, sum+1):
    if i == nums[0]:
      result[i] = True

  for i in range(1, len(nums)):
    for j in range(sum, -1, -1):
      if result[j]:
        result[j] = True
      elif nums[i] <= j:
        result[j] = result[j - nums[i]]

  return result[sum]

def main():
    print("Can partition: " + str(can_partition([1, 2, 3, 7], 6)))
    print("Can partition: " + str(can_partition([1, 2, 7, 1, 5], 10)))
    print("Can partition: " + str(can_partition([1, 3, 4, 8], 6)))

main()
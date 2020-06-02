from collections import deque


def find_permutations(nums):
  '''
  Given a set of distinct numbers, find all of its permutations.
  '''
  result = []
  permutate(nums, 0, [], result)
  return result

def permutate(nums, i, current, result):
  if i == len(nums):
    result.append(current)
    return

  for l in range(len(current) + 1):
    next = list(current)
    next.insert(l, nums[i])
    permutate(nums, i + 1, next, result)



def main():
  print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()

from collections import deque

def find_permutations(nums):
    '''
    Given a set of distinct numbers, find all of its permutations.
    '''
    result = []
    queue = deque()
    queue.append([])

    for num in nums:
        queue_size = len(queue)

        for _ in range(queue_size):
            curr = queue.popleft()

            for i in range(len(curr) + 1):
                next = list(curr)
                next.insert(i, num)
                queue.append(next)

    return list(queue)


def main():
    print("Here are all the permutations: " + str(find_permutations([1, 3, 5])))


main()

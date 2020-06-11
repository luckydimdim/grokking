from heapq import *
from collections import deque

def schedule_tasks(tasks, k):
    '''
    You are given a list of tasks that need to be run, in any order, on a server.
    Each task will take one CPU interval to execute but once a task has finished,
    it has a cooling period during which it can’t be run again.
    If the cooling period for all tasks is ‘K’ intervals,
    find the minimum number of CPU intervals that the server needs to finish all tasks.
    If at any time the server can’t execute any task then it must stay idle.
    '''
    result = 0
    hash_map = {}
    for task in tasks:
        hash_map[task] = hash_map.get(task, 0) + 1

    max_heap = []
    for task, rate in hash_map.items():
        heappush(max_heap, (-rate, task))

    queue = deque()

    while max_heap:
        counter = k + 1

        while counter > 0 and max_heap:
            result += 1
            rate, task = heappop(max_heap)

            if -rate > 1:
                queue.append((rate+1, task))

            counter -= 1

        while queue:
            heappush(max_heap, queue.popleft())

        if max_heap:
            result += counter

    return result

def main():
    print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum intervals needed to execute all tasks: " +
        str(schedule_tasks(['a', 'b', 'a'], 3)))


main()


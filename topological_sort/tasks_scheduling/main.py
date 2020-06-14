from collections import deque

def is_scheduling_possible(tasks, prerequisites):
    '''
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
    Each task can have some prerequisite tasks which
    need to be completed before it can be scheduled.
    Given the number of tasks and a list of prerequisite pairs,
    find out if it is possible to schedule all the tasks.
    '''
    result = []

    in_degree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for prerequisite in prerequisites:
        parent, child = prerequisite[0], prerequisite[1]
        graph[parent].append(child)
        in_degree[child] += 1

    queue = deque()
    for vertex in in_degree:
        if vertex == 0:
            queue.append(vertex)

    while queue:
        node = queue.popleft()
        result.append(node)
        for child in graph[node]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    return len(result) == tasks

def main():
    print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2]])))
    print("Is scheduling possible: " +
        str(is_scheduling_possible(3, [[0, 1], [1, 2], [2, 0]])))
    print("Is scheduling possible: " +
        str(is_scheduling_possible(6, [[0, 4], [1, 4], [3, 2], [1, 3]])))

main()

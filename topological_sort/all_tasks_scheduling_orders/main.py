from collections import deque

def print_orders(tasks, prerequisites):
    '''
    There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’.
    Each task can have some prerequisite tasks which
    need to be completed before it can be scheduled.
    Given the number of tasks and a list of prerequisite pairs,
    write a method to print all possible ordering of tasks meeting all prerequisites.
    '''
    result = []
    in_degree = {i: 0 for i in range(tasks)}
    graph = {i: [] for i in range(tasks)}

    for prerequisite in prerequisites:
        parent, child = prerequisite
        graph[parent].append(child)
        in_degree[child] += 1

    queue = deque()
    for child in in_degree:
        if child == 0:
            queue.append(child)

    print_all_topological_sorts(graph, in_degree, queue, result)

    return result

def print_all_topological_sorts(graph, in_degree, queue, result):
    if queue:
        for vertex in queue:
            result.append(vertex)
            next = deque(queue)
            next.remove(vertex)

            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 0:
                    next.append(child)

            print_all_topological_sorts(graph, in_degree, next, result)

            result.remove(vertex)
            for child in graph[vertex]:
                in_degree[child] += 1

    if len(result) == len(in_degree):
        print(result)

def main():
    print("Task Orders: ")
    print_orders(3, [[0, 1], [1, 2]])

    print("Task Orders: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])

    print("Task Orders: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])

main()

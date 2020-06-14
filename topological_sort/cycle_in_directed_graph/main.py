from collections import deque

def topological_sort(vertices, edges):
    '''
    Find if a given Directed Graph has a cycle in it or not
    '''
    result = []

    in_degree = {i: 0 for i in range(vertices)}
    graph = {i: [] for i in range(vertices)}

    for edge in edges:
        parent, child = edge[0], edge[1]
        graph[parent].append(child)
        in_degree[child] += 1

    queue = deque()
    for vertice in in_degree:
        if in_degree[vertice] == 0:
            queue.append(vertice)

    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                queue.append(child)

    return len(result) == vertices

def main():
    print("Topological sort: " +
        str(topological_sort(4, [[3, 2], [3, 0], [2, 0], [2, 1]])))
    print("Topological sort: " +
        str(topological_sort(5, [[4, 2], [4, 3], [2, 0], [2, 1], [3, 1]])))
    print("Topological sort: " +
        str(topological_sort(7, [[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]])))

main()

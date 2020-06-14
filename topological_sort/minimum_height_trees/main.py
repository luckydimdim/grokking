from collections import deque

def find_trees(nodes, edges):
    '''
    We are given an undirected graph that has characteristics of a k-ary tree.
    In such a graph, we can choose any node as the root to make a k-ary tree.
    The root (or the tree) with the minimum height will be called Minimum Height Tree (MHT).
    There can be multiple MHTs for a graph. In this problem,
    we need to find all those roots which give us MHTs.
    Write a method to find all MHTs of the given graph and return a list of their roots.
    '''
    if nodes <= 0:
        return []

    if nodes == 1:
        return [0]

    in_degree = {i: 0 for i in range(nodes)}
    graph = {i: [] for i in range(nodes)}

    for edge in edges:
        n1, n2 = edge[0], edge[1]
        graph[n1].append(n2)
        graph[n2].append(n1)
        in_degree[n1] += 1
        in_degree[n2] += 1

    leaves = deque()
    for key in in_degree:
        if in_degree[key] == 1:
            leaves.append(key)

    total_nodes = nodes
    while total_nodes > 2:
        leaves_size = len(leaves)
        total_nodes -= leaves_size
        for i in range(leaves_size):
            vertex = leaves.popleft()
            for child in graph[vertex]:
                in_degree[child] -= 1
                if in_degree[child] == 1:
                    leaves.append(child)

    return list(leaves)

def main():
    print("Roots of MHTs: " +
        str(find_trees(5, [[0, 1], [1, 2], [1, 3], [2, 4]])))
    print("Roots of MHTs: " +
        str(find_trees(4, [[0, 1], [0, 2], [2, 3]])))
    print("Roots of MHTs: " +
        str(find_trees(4, [[1, 2], [1, 3]])))


main()

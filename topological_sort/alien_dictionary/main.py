from collections import deque

def find_order(words):
    '''
    There is a dictionary containing words from an alien language for
    which we don’t know the ordering of the characters.
    Write a method to find the correct order of characters in the alien language.
    '''
    result = ''
    if len(words) == 0:
        return result

    in_degree = {}
    graph = {}
    for word in words:
        for letter in word:
            in_degree[letter] = 0
            graph[letter] = []

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        for j in range(min(len(w1), len(w2))):
            parent, child = w1[j], w2[j]
            if parent != child:
                graph[parent].append(child)
                in_degree[child] += 1
                break

    print(graph)
    print(in_degree)

    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    ordered = []
    while sources:
        vertex = sources.popleft()
        ordered.append(vertex)
        for child in graph[vertex]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    if len(ordered) != len(in_degree):
        return ''

    return ''.join(ordered)


def main():
    print("Character order: " + find_order(["ba", "bc", "ac", "cab"]))
    print("Character order: " + find_order(["cab", "aaa", "aab"]))
    print("Character order: " + find_order(["ywx", "wz", "xww", "xz", "zyy", "zwz"]))

main()

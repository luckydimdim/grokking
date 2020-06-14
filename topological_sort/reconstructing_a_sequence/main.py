from collections import deque

def can_construct(original_seq, sequences):
    '''
    Given a sequence originalSeq and an array of sequences,
    write a method to find if originalSeq can be
    uniquely reconstructed from the array of sequences.
    Unique reconstruction means that
    we need to find if originalSeq is the only sequence such that
    all sequences in the array are subsequences of it.
    '''
    result = []
    if len(original_seq) == 0:
        return False

    graph, in_degree = {}, {}

    for sequence in sequences:
        for num in sequence:
            in_degree[num] = 0
            graph[num] = []

    for sequence in sequences:
        for i in range(1, len(sequence)):
            parent, child = sequence[i - 1], sequence[i]
            graph[parent].append(child)
            in_degree[child] += 1

    if len(in_degree) != len(original_seq):
        return False

    sources = deque()
    for key in in_degree:
        if in_degree[key] == 0:
            sources.append(key)

    while sources:
        if len(sources) > 1:
            return False

        if original_seq[len(result)] != sources[0]:
            return False

        source = sources.popleft()
        result.append(source)
        for child in graph[source]:
            in_degree[child] -= 1
            if in_degree[child] == 0:
                sources.append(child)

    return len(result) == len(original_seq)

def main():
    print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [3, 4]])))
    print("Can construct: " +
        str(can_construct([1, 2, 3, 4], [[1, 2], [2, 3], [2, 4]])))
    print("Can construct: " +
        str(can_construct([3, 1, 4, 2, 5], [[3, 1, 5], [1, 4, 2, 5]])))


main()

def merge(intervals_a, intervals_b):
    '''
    Given two lists of intervals, find the intersection of these two lists.
    Each list consists of disjoint intervals sorted on their start time.
    '''
    result = []
    a, b = 0, 0
    start, end = 0, 1

    while a < len(intervals_a) and b < len(intervals_b):
        a_overlaps_b = intervals_a[a][start] >= intervals_b[b][start] and \
            intervals_a[a][start] <= intervals_b[b][end]

        b_overlaps_a = intervals_b[b][start] >= intervals_a[a][start] and \
            intervals_b[b][start] <= intervals_a[a][end]

        if a_overlaps_b or b_overlaps_a:
            intersection_start = max(intervals_a[a][start], intervals_b[b][start])
            intersection_end = min(intervals_a[a][end], intervals_b[b][end])
            result.append([intersection_start, intersection_end])

        if intervals_a[a][end] < intervals_b[b][end]:
            a += 1
        else:
            b += 1

    return result


# [1, 3], [5, 6], [7, 9]
# [2, 3], [5, 7]

# [1, 3], [5, 7], [9, 12]
# [5, 10]

def main():
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
    print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))

main()

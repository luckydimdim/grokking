def insert2(intervals, new_interval):
    '''
    Given a list of non-overlapping intervals sorted by their start time,
    insert a given interval at the correct position and merge all necessary intervals
    to produce a list that has only mutually exclusive intervals.
    '''
    merged = []
    index = 0

    while new_interval[0] > intervals[index][0]:
        merged.append(intervals[index])
        index += 1

    intervals.insert(index, new_interval)

    start, end = intervals[index][0], intervals[index][1]

    for i in range(index + 1, len(intervals)):
        interval = intervals[i]

        if interval[0] <= end:
            end = max(interval[1], end)
        else:
            merged.append([start, end])
            start, end = interval[0], interval[1]

    merged.append([start, end])

    return merged

def insert3(intervals, new_interval):
    '''
    Given a list of non-overlapping intervals sorted by their start time,
    insert a given interval at the correct position and merge all necessary intervals
    to produce a list that has only mutually exclusive intervals.
    '''
    merged = []
    i, start, end = 0, 0, 1

    while i < len(intervals) and intervals[i][end] < new_interval[start]:
        merged.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][start] <= new_interval[end]:
        new_interval[start] = min(new_interval[start], intervals[i][start])
        new_interval[end] = max(new_interval[end], intervals[i][end])
        i += 1

    merged.append(new_interval)

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged

def insert(intervals, new_interval):
    '''
    Given a list of non-overlapping intervals sorted by their start time,
    insert a given interval at the correct position and merge all necessary intervals
    to produce a list that has only mutually exclusive intervals.
    '''
    merged = []
    counter, start, end = 0, 0, 1

    while counter < len(intervals) and intervals[counter][end] < new_interval[start]:
        merged.append(intervals[counter])
        counter += 1

    while counter < len(intervals) and new_interval[end] >= intervals[counter][start]:
        new_interval[start] = min(new_interval[start], intervals[counter][start])
        new_interval[end] = max(new_interval[end], intervals[counter][end])
        counter += 1

    merged.append(new_interval)

    while counter < len(intervals):
        merged.append(intervals[counter])
        counter += 1

    return merged

def main():
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
  print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
  print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))


main()

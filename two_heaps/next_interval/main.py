from heapq import *

class Interval:
  def __init__(self, start, end):
    self.start = start
    self.end = end


def find_next_interval(intervals):
  '''
  Given an array of intervals, find the next interval of each interval.
  In a list of intervals, for an interval ‘i’ its next interval ‘j’
  will have the smallest ‘start’ greater than or equal to the ‘end’ of ‘i’.
  Write a function to return an array containing indices of the next interval
  of each input interval. If there is no next interval of a given interval, return -1.
  It is given that none of the intervals have the same start point.
  '''
  n = len(intervals)
  result = [0 for x in range(n)]
  max_start_heap, max_finish_heap = [], []

  for end_index in range(n):
    heappush(max_start_heap, (-intervals[end_index].start, end_index))
    heappush(max_finish_heap, (-intervals[end_index].end, end_index))

  for _ in range(n):
    top_finish, end_index = heappop(max_finish_heap)
    result[end_index] = -1

    if -max_start_heap[0][0] >= -top_finish:
      top_start, start_index = heappop(max_start_heap)

      while max_start_heap and max_start_heap[0][0] >= -top_finish:
        top_start, start_index = heappop(max_start_heap)

      result[end_index] = start_index
      heappush(max_start_heap, (top_start, start_index))

  return result


def main():

  result = find_next_interval(
    [Interval(2, 3), Interval(3, 4), Interval(5, 6)])
  print("Next interval indices are: " + str(result))

  result = find_next_interval(
    [Interval(3, 4), Interval(1, 5), Interval(4, 6)])
  print("Next interval indices are: " + str(result))


main()

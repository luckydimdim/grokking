from heapq import *
import heapq

class SlidingWindowMedian:

  def find_sliding_window_median(self, nums, k):
    '''
    Given an array of numbers and a number ‘k’,
    find the median of all the ‘k’ sized sub-arrays (or windows) of the array.
    '''
    result = []
    window_start = 0
    min_heap, max_heap = [], []
    for window_end in range(len(nums)):
      if not max_heap or -max_heap[0] >= nums[window_end]:
        heappush(max_heap, -nums[window_end])
      else:
        heappush(min_heap, nums[window_end])

      if len(max_heap) > len(min_heap) + 1:
        heappush(min_heap, -heappop(max_heap))
      elif len(max_heap) < len(min_heap):
        heappush(max_heap, -heappop(min_heap))

      if window_end - window_start + 1 >= k:
        if len(min_heap) == len(max_heap):
          result.append(-max_heap[0] / 2.0 + min_heap[0] / 2.0)
        else:
          result.append(-max_heap[0] / 1.0)

        if nums[window_start] <= -max_heap[0]:
          index = max_heap.index(-nums[window_start])
          max_heap[index] = max_heap[-1]
          del max_heap[-1]
          if index < len(max_heap):
            heapq._siftup(max_heap, index)
            heapq._siftdown(max_heap, 0, index)
        else:
          index = min_heap.index(nums[window_start])
          min_heap[index] = min_heap[-1]
          del min_heap[-1]
          if index < len(min_heap):
            heapq._siftup(min_heap, index)
            heapq._siftdown(min_heap, 0, index)

        if len(max_heap) > len(min_heap) + 1:
          heappush(min_heap, -heappop(max_heap))
        elif len(max_heap) < len(min_heap):
          heappush(max_heap, -heappop(min_heap))

        window_start += 1

    return result

def main():

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 2)
  print("Sliding window medians are: " + str(result))

  slidingWindowMedian = SlidingWindowMedian()
  result = slidingWindowMedian.find_sliding_window_median(
    [1, 2, -1, 3, 5], 3)
  print("Sliding window medians are: " + str(result))


main()

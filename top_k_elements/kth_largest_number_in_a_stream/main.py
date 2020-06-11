from heapq import *

class KthLargestNumberInStream:
  '''
  Design a class to efficiently find the Kth largest element in a stream of numbers.
  The class should have the following two things:
  The constructor of the class should accept an integer array
  containing initial numbers from the stream and an integer ‘K’.
  The class should expose a function add(int num)
  which will store the given number and return the Kth largest number.
  '''
  def __init__(self, nums, k):
    self.min_heap = []
    self.k = k

    for num in nums:
      self.add(num)

  def add(self, num):
    heappush(self.min_heap, num)

    if len(self.min_heap) > self.k:
      heappop(self.min_heap)

    return self.min_heap[0]

def main():
  kthLargestNumber = KthLargestNumberInStream([3, 1, 5, 12, 2, 11], 4)
  print("4th largest number is: " + str(kthLargestNumber.add(6)))
  print("4th largest number is: " + str(kthLargestNumber.add(13)))
  print("4th largest number is: " + str(kthLargestNumber.add(4)))

main()


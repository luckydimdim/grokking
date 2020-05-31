from heapq import *

class MedianOfAStream:
  '''
  Design a class to calculate the median of a number stream. The class should have the following two methods:
    insertNum(int num): stores the number in the class
    findMedian(): returns the median of all numbers inserted in the class
  If the count of numbers inserted in the class is even, the median will be the average of the middle two numbers.
  '''
  min_heap = []
  max_heap = []

  def insert_num(self, num):
    if not self.max_heap or -self.max_heap[0] >= num:
      heappush(self.max_heap, -num)
    else:
      heappush(self.min_heap, num)

    if len(self.max_heap) > len(self.min_heap) + 1:
      heappush(self.min_heap, -heappop(self.max_heap))
    elif len(self.max_heap) < len(self.min_heap):
      heappush(self.max_heap, -heappop(self.min_heap))

  def find_median(self):
    if len(self.min_heap) == len(self.max_heap):
      return -self.max_heap[0] / 2.0 + self.min_heap[0] / 2.0

    return -self.max_heap[0] / 1.0

def main():
  medianOfAStream = MedianOfAStream()
  medianOfAStream.insert_num(3)
  medianOfAStream.insert_num(1)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(5)
  print("The median is: " + str(medianOfAStream.find_median()))
  medianOfAStream.insert_num(4)
  print("The median is: " + str(medianOfAStream.find_median()))


main()

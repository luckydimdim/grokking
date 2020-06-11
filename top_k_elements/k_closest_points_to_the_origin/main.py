from heapq import *
import math

class Point:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __lt__(self, other):
    return self.distance_from_origin() > other.distance_from_origin()

  def print_point(self):
    print("[" + str(self.x) + ", " + str(self.y) + "] ", end='')

  def distance_from_origin(self):
    return self.x*self.x + self.y*self.y

def find_closest_points2(points, k):
  '''
  Given an array of points in the a 2D plane,
  find ‘K’ closest points to the origin.
  '''
  max_heap = []

  for i in range(len(points)):
    distance = math.sqrt(points[i].x*points[i].x + points[i].y*points[i].y)

    if i < k:
      heappush(max_heap, (-distance, points[i]))
    else:
      if -distance > max_heap[0][0]:
        heappop(max_heap)
        heappush(max_heap, (-distance, points[i]))

  return [x[1] for x in list(max_heap)]

def find_closest_points(points, k):
  max_heap = []

  for i in range(k):
    heappush(max_heap, points[i])

  for i in range(k, len(points)):
    if points[i].distance_from_origin() < max_heap[0].distance_from_origin():
      heappop(max_heap)
      heappush(max_heap, points[i])

  return list(max_heap)

def main():
  result = find_closest_points([Point(1, 3), Point(3, 4), Point(2, -1)], 2)
  print("Here are the k points closest the origin: ", end='')
  for point in result:
    point.print_point()


main()



from heapq import *

class Meeting:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def __lt__(self, other):
    return self.end < other.end

def min_meeting_rooms2(meetings):
  '''
  Given a list of intervals representing the start and end time of ‘N’ meetings,
  find the minimum number of rooms required to hold all the meetings.
  '''
  rooms_needed = 0
  meetings.sort(key = lambda x: x.start)
  min_heap = []

  for meeting in meetings:
    while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
      heappop(min_heap)

    heappush(min_heap, meeting)

    rooms_needed = max(rooms_needed, len(min_heap))

  return rooms_needed

def min_meeting_rooms3(meetings):
  '''
  Given a list of intervals representing the start and end time of ‘N’ meetings,
  find the minimum number of rooms required to hold all the meetings.
  '''
  meetings.sort(key = lambda x: x.start)
  min_rooms = 0
  min_heap = []

  for meeting in meetings:
    while len(min_heap) > 0 and meeting.start >= min_heap[0].end:
      heappop(min_heap)

    heappush(min_heap, meeting)

    min_rooms = max(min_rooms, len(min_heap))

  return min_rooms

def min_meeting_rooms(meetings):
  '''
  Given a list of intervals representing the start and end time of ‘N’ meetings,
  find the minimum number of rooms required to hold all the meetings.
  '''
  min_rooms = 0
  meetings.sort(key = lambda x: x.start)
  min_heap = []

  for i in range(len(meetings)):
    while len(min_heap) > 0 and min_heap[0].end <= meetings[i].start:
      heappop(min_heap)

    heappush(min_heap, meetings[i])

    min_rooms = max(min_rooms, len(min_heap))

  return min_rooms

def main():
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))


main()

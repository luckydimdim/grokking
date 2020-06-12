from __future__ import print_function
from heapq import *

class ListNode:
  def __init__(self, value):
    self.value = value
    self.next = None

  def __lt__(self, other):
    return self.value < other.value

def merge_lists2(lists):
  '''
  Given an array of ‘K’ sorted LinkedLists,
  merge them into one sorted list.
  '''
  result = None
  min_heap = []

  for i in range(len(lists)):
    heappush(min_heap, (lists[i].value, i))

  node = heappop(min_heap)
  result = ListNode(node[0])
  lists[node[1]] = lists[node[1]].next
  heappush(min_heap, (lists[node[1]].value, node[1]))
  curr = result

  while lists and min_heap:
    node = heappop(min_heap)
    curr.next = ListNode(node[0])
    curr = curr.next
    lists[node[1]] = lists[node[1]].next

    if lists[node[1]]:
      heappush(min_heap, (lists[node[1]].value, node[1]))

  return result

def merge_lists(lists):
  result = []
  min_heap = []

  for node in lists:
    heappush(min_heap, node)

  head, tail = None, None
  while min_heap:
    node = heappop(min_heap)
    if head is None:
      head = tail = node
    else:
      tail.next = node
      tail = tail.next

    if node.next is not None:
      heappush(min_heap, node.next)

  return head

def main():
  l1 = ListNode(2)
  l1.next = ListNode(6)
  l1.next.next = ListNode(8)

  l2 = ListNode(3)
  l2.next = ListNode(6)
  l2.next.next = ListNode(7)

  l3 = ListNode(1)
  l3.next = ListNode(3)
  l3.next.next = ListNode(4)

  result = merge_lists([l1, l2, l3])
  print("Here are the elements form the merged list: ", end='')
  while result != None:
    print(str(result.value) + " ", end='')
    result = result.next

main()


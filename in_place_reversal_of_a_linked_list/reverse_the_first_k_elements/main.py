from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end=" ")
      temp = temp.next
    print()

def reverse_sub_list(head, k):
  '''
  Reverse the first ‘k’ elements of a given LinkedList
  '''
  if k == 1:
    return head

  prev, curr = None, head

  while curr is not None and k > 0:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    k -= 1

  head.next = curr
  head = prev

  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

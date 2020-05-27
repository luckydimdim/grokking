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

def reverse_sub_list(head):
  '''
  Given a LinkedList with ‘n’ nodes, reverse it based on its size in the following way:
    - If ‘n’ is even, reverse the list in a group of n/2 nodes.
    - If n is odd, keep the middle node as it is, reverse the first ‘n/2’ nodes and reverse the last ‘n/2’ nodes.
  '''
  counter, curr = 0, head

  while curr is not None:
    curr = curr.next
    counter += 1

  # even
  if counter % 2 == 0:
    curr, prev = head, None
    middle = counter // 2
    counter = 0

    while counter < middle:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
      counter += 1

    head.next = curr

    return prev
  # odd
  else:
    middle = counter // 2
    counter = 0
    curr, prev = head, None

    while counter < middle:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
      counter += 1

    head.next = curr
    head = prev

    head_of_second_part = curr
    curr, prev = curr.next, None

    while curr is not None:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next

    head_of_second_part.next = prev

  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

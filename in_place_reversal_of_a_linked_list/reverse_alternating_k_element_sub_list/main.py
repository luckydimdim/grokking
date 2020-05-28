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


def reverse_alternate_k_elements2(head, k):
  '''
  Given the head of a LinkedList and a number ‘k’,
  reverse every alternating ‘k’ sized sub-list starting from the head.
  If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
  '''
  if head is None or k <= 1:
    return head

  curr, prev = head, None
  is_new_head = False

  while True:
    tail = prev
    end = curr

    counter = 0
    while counter < k and curr is not None:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
      counter += 1

    if is_new_head == False:
      is_new_head = True
      head = prev

    if tail is not None:
      tail.next = prev

    end.next = curr

    counter = 0
    while counter < k and curr is not None:
      prev = curr
      curr = curr.next
      counter += 1

    if curr is None:
      break

  return head

def reverse_alternate_k_elements(head, k):
  '''
  Given the head of a LinkedList and a number ‘k’,
  reverse every alternating ‘k’ sized sub-list starting from the head.
  If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.
  '''
  if head is None or k <= 1:
    return head

  prev, curr = None, head
  is_head = False

  while True:
    end = curr
    tail = prev

    counter = 0
    while counter < k and curr is not None:
      counter += 1
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next

    if is_head == False:
      is_head = True
      head = prev

    if tail is not None:
      tail.next = prev

    end.next = curr

    counter = 0
    while counter < k and curr is not None:
      counter += 1
      prev = curr
      curr = curr.next

    if curr is None:
      break

  return head


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  head.next.next.next.next.next.next = Node(7)
  head.next.next.next.next.next.next.next = Node(8)
  head.next.next.next.next.next.next.next.next = Node(9)
  head.next.next.next.next.next.next.next.next.next = Node(10)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_alternate_k_elements(head, 2)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

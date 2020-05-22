from __future__ import print_function


class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(str(temp.value) + " ", end='')
      temp = temp.next
    print()


def reorder(head):
  '''
  Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes
  from the second half of the LinkedList are inserted alternately to the nodes from the first half
  in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null,
  your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.
  Your algorithm should not use any extra space and the input LinkedList should be modified in-place.
  '''
  slow, fast = head, head

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  first_head = head
  second_head = reverse_linked_list(slow)

  while first_head is not None and second_head is not None:
    first_next = first_head.next
    first_head.next = second_head
    first_head = first_next

    second_next = second_head.next
    second_head.next = first_head
    second_head = second_next

  if first_head is not None:
    first_head.next = None

  return head

def reverse_linked_list(head):
  prev = None

  while head is not None:
    next = head.next
    head.next = prev
    prev = head
    head = next

  return prev


def main():
  head = Node(2)
  head.next = Node(4)
  head.next.next = Node(6)
  head.next.next.next = Node(8)
  head.next.next.next.next = Node(10)
  head.next.next.next.next.next = Node(12)
  reorder(head)
  head.print_list()


main()

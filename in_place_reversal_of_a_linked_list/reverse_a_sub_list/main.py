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


def reverse_sub_list2(head, p, q):
  '''
  Given the head of a LinkedList and two positions ‘p’ and ‘q’,
  reverse the LinkedList from position ‘p’ to ‘q’.
  '''
  if p == q:
    return head

  curr, prev, counter = head, None, 0

  while curr is not None and counter < p - 1:
    counter += 1
    prev = curr
    curr = curr.next

  last_node_of_first_part = prev
  last_node_of_sublist = curr

  while curr is not None and counter < q:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    counter += 1

  if last_node_of_first_part is not None:
    last_node_of_first_part.next = prev
  else:
    head = prev

  last_node_of_sublist.next = curr

  return head

def reverse_sub_list3(head, p, q):
  '''
  Given the head of a LinkedList and two positions ‘p’ and ‘q’,
  reverse the LinkedList from position ‘p’ to ‘q’.
  '''
  if p == q:
    return head

  prev, curr, counter = None, head, 0

  while curr is not None and counter < p - 1:
    prev = curr
    curr = curr.next
    counter += 1

  tail_of_first_part = prev
  tail_of_mid_part = curr

  while curr is not None and counter < q:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    counter += 1

  if tail_of_first_part is not None:
    tail_of_first_part.next = prev
  else:
    head = prev

  tail_of_mid_part.next = curr

  return head

def reverse_sub_list(head, p, q):
  '''
  Given the head of a LinkedList and two positions ‘p’ and ‘q’,
  reverse the LinkedList from position ‘p’ to ‘q’.
  '''
  if p == q or head is None:
    return head

  counter, prev, curr = 0, None, head
  while counter < p - 1 and curr is not None:
    prev = curr
    curr = curr.next
    counter += 1

  tail_of_first_half = prev
  tail_of_second_half = curr

  prev = None
  while curr is not None and counter < q:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next
    counter += 1

  if tail_of_first_half is not None:
    tail_of_first_half.next = prev
  else:
    head = prev

  tail_of_second_half.next = curr

  return head

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_sub_list(head, 2, 4)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

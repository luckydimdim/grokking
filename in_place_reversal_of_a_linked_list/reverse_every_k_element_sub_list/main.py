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


def reverse_every_k_elements2(head, k):
  '''
  Given the head of a LinkedList and a number ‘k’,
  reverse every ‘k’ sized sub-list starting from the head.
  If, in the end, you are left with a sub-list with
  less than ‘k’ elements, reverse it too.
  '''
  if k <= 1 or head is None:
    return head

  curr, prev, new_head = head, None, False

  while True:
    last_node_of_previous_part = prev
    last_node_of_sub_list = curr

    counter = 0
    while counter < k and curr is not None:
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next
      counter += 1

    # connect with the previous part
    if last_node_of_previous_part is not None:
      last_node_of_previous_part.next = prev

    if new_head == False:
      new_head = True
      head = prev

    # connect with the next part
    last_node_of_sub_list.next = curr

    if curr is None:
      break

    prev = last_node_of_sub_list

  return head

def reverse_every_k_elements(head, k):
  '''
  Given the head of a LinkedList and a number ‘k’,
  reverse every ‘k’ sized sub-list starting from the head.
  If, in the end, you are left with a sub-list with
  less than ‘k’ elements, reverse it too.
  '''
  if k <= 1 or head is None:
    return head

  counter, prev, curr = 0, None, head
  is_new_head = False

  while True:
    link = prev
    tail = curr

    counter = 0
    while counter < k and curr is not None:
      counter += 1
      next = curr.next
      curr.next = prev
      prev = curr
      curr = next

    if is_new_head == False:
      head = prev
      is_new_head = True

    if link is not None:
      link.next = prev

    tail.next = curr

    if curr is None:
      break

    prev = tail

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

  print("Nodes of original LinkedList are: ", end='')
  head.print_list()
  result = reverse_every_k_elements(head, 3)
  print("Nodes of reversed LinkedList are: ", end='')
  result.print_list()


main()

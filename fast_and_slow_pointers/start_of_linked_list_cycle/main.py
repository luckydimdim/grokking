from __future__ import print_function

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

  def print_list(self):
    temp = self
    while temp is not None:
      print(temp.value, end='')
      temp = temp.next
    print()

def find_cycle_start(head):
  '''
  Given the head of a Singly LinkedList that contains a cycle,
  write a function to find the starting node of the cycle.
  '''

  slow, fast = head, head
  cursor = None
  length = 0
  counter = 0

  while fast is not None and fast.next is not None and fast.next.next is not None:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
      cursor = slow

      while True:
        counter += 1
        cursor = cursor.next

        if cursor == slow:
          break
      break

  slow, fast = head, head

  while counter > 0:
    fast = fast.next
    counter -= 1

  while slow != fast:
    slow = slow.next
    fast = fast.next

  return slow

def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))

  head.next.next.next.next.next.next = head
  print("LinkedList cycle start: " + str(find_cycle_start(head).value))


main()

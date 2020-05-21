class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def cycle_length(head):
  slow, fast = head, head
  pointer = None
  counter = 0

  while not fast is None and not fast.next is None and not fast.next.next is None:
    fast = fast.next.next
    slow = slow.next

    if slow == fast:
      pointer = slow

      while True:
        pointer = pointer.next
        counter += 1

        if pointer == slow:
          return counter

  return 0


def main():
  head = Node(1)
  head.next = Node(2)
  head.next.next = Node(3)
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(5)
  head.next.next.next.next.next = Node(6)
  print("LinkedList cycle length: " + str(cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next
  print("LinkedList cycle length: " + str(cycle_length(head)))

  head.next.next.next.next.next.next = head.next.next.next
  print("LinkedList cycle length: " + str(cycle_length(head)))


main()

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def is_palindromic_linked_list2(head):
  '''
  Given the head of a Singly LinkedList, write a method
  to check if the LinkedList is a palindrome or not.
  Your algorithm should use constant space
  and the input LinkedList should be in the original form once the algorithm is finished.
  The algorithm should have O(N) time complexity
  where ‘N’ is the number of nodes in the LinkedList.
  '''
  slow, fast = head, head

  while not fast is None and not fast.next is None:
    slow = slow.next
    fast = fast.next.next

  head_second_half = reverse(slow)
  copy_head_second_half = head_second_half

  while head is not None and head_second_half is not None:
    if head.value != head_second_half.value:
      break

    head = head.next
    head_second_half = head_second_half.next

  reverse(copy_head_second_half)

  if head is None and head_second_half is None:
    return True

  return False

def reverse(head):
  prev, next, curr = None, None, head

  while curr is not None:
    next = curr.next
    curr.next = prev
    prev = curr
    curr = next

  return prev

def is_palindromic_linked_list(head):
  '''
  Given the head of a Singly LinkedList, write a method
  to check if the LinkedList is a palindrome or not.
  Your algorithm should use constant space
  and the input LinkedList should be in the original form once the algorithm is finished.
  The algorithm should have O(N) time complexity
  where ‘N’ is the number of nodes in the LinkedList.
  '''
  slow, fast = head, head

  while fast is not None and fast.next is not None:
    slow = slow.next
    fast = fast.next.next

  reversed_middle = reverse_linked_list(slow)
  copy_reversed_middle = reversed_middle

  while reversed_middle is not None:
    if head.value != reversed_middle.value:
      break

    reversed_middle = reversed_middle.next
    head = head.next

  reverse_linked_list(copy_reversed_middle)

  if reversed_middle is None and head is None:
    return True

  return False

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
  head.next.next.next = Node(4)
  head.next.next.next.next = Node(2)

  print("Is palindrome: " + str(is_palindromic_linked_list(head)))

  head.next.next.next.next.next = Node(2)
  print("Is palindrome: " + str(is_palindromic_linked_list(head)))


main()

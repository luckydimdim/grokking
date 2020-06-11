from heapq import *

class Element:
  def __init__(self, num, rate, seq):
    self.num = num
    self.rate = rate
    self.seq = seq

  def __lt__(self, other):
    if self.rate != other.rate:
      return self.rate > other.rate

    return self.seq > other.seq

class FrequencyStack:
  def __init__(self):
    self.hash_map = {}
    self.seq = 0
    self.max_heap = []

  def push(self, num):
    '''
    Design a class that simulates a Stack data structure,
    implementing the following two operations:
    push(int num): Pushes the number ‘num’ on the stack.
    pop(): Returns the most frequent number in the stack.
    If there is a tie, return the number which was pushed later.
    '''
    self.hash_map[num] = self.hash_map.get(num, 0) + 1
    heappush(self.max_heap, Element(num, self.hash_map[num], self.seq))
    self.seq += 1

  def pop(self):
    num = heappop(self.max_heap).num

    if self.hash_map[num] > 1:
      self.hash_map[num] -= 1
    else:
      del self.hash_map[num]

    return num

def main():
  frequencyStack = FrequencyStack()
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(3)
  frequencyStack.push(2)
  frequencyStack.push(1)
  frequencyStack.push(2)
  frequencyStack.push(5)
  print(frequencyStack.pop())
  print(frequencyStack.pop())
  print(frequencyStack.pop())


main()








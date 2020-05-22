def find_happy_number2(num):
  '''
  Any number will be called a happy number if, after repeatedly replacing it
  with a number equal to the sum of the square of all of its digits,
  leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’.
  Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
  '''

  uniques = {}

  return check(num, uniques)

def check(num, uniques):
    digits = []

    while num > 0:
        digits.append(num % 10)
        num = num // 10

    for i in range(len(digits)):
        digits[i] *= digits[i]

    current_sum = sum(digits)

    if current_sum == 1:
        return True

    if current_sum in uniques:
        return False

    uniques[current_sum] = True

    return check(current_sum, uniques)

def find_happy_number(num):
  '''
  Any number will be called a happy number if, after repeatedly replacing it
  with a number equal to the sum of the square of all of its digits,
  leads us to number ‘1’. All other (not-happy) numbers will never reach ‘1’.
  Instead, they will be stuck in a cycle of numbers which does not include ‘1’.
  '''

  slow, fast = num, num

  while True:
    slow = sum_digits(slow)
    fast = sum_digits(sum_digits(fast))

    if slow == fast:
        break

  return slow == 1

def sum_digits(num):
    result = 0

    while num > 0:
        square = num % 10
        result += square * square
        num //= 10

    return result

def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()



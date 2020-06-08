from collections import deque

def generate_valid_parentheses2(nums):
    '''
    For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
    '''
    queue = deque()
    queue.append([])
    for i in range(nums):
        queue_size = len(queue)
        for _ in range(queue_size):
            curr = queue.popleft()
            for c in range(len(curr) + 1):
                next = list(curr)
                next.insert(c, '()')
                queue.append(''.join(next))

    return list(set(queue))

class ParenthesesString:
    def __init__(self, value, opened, closed):
        self.value = value
        self.opened = opened
        self.closed = closed


def generate_valid_parentheses3(nums):
    '''
    For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.
    N = 3, ((())), (()()), (())(), ()(()), ()()()
    '''
    result = []
    queue = deque()
    queue.append(ParenthesesString('', 0, 0))

    while queue:
        curr = queue.popleft()

        if curr.opened == nums and curr.closed == nums:
            result.append(curr.value)
        else:
            if curr.opened < nums:
                queue.append(ParenthesesString(curr.value + '(', curr.opened + 1, curr.closed))

            if curr.opened > curr.closed:
                queue.append(ParenthesesString(curr.value + ')', curr.opened, curr.closed + 1))

    return result

class Bracket:
    def __init__(self, value, opened, closed):
        self.value = value
        self.opened = opened
        self.closed = closed

def generate_valid_parentheses(nums):
    '''
    For a given number ‘N’, write a function to
    generate all combination of ‘N’ pairs of balanced parentheses.
    N = 3, ((())), (()()), (())(), ()(()), ()()()
    '''
    result = []
    queue = deque()
    queue.append(Bracket('', 0, 0))
    while queue:
        curr = queue.popleft()
        if curr.opened == nums and curr.closed == nums:
            result.append(curr.value)
        else:
            if curr.opened < nums:
                queue.append(Bracket(curr.value + '(', curr.opened + 1, curr.closed))

            if curr.closed < curr.opened:
                queue.append(Bracket(curr.value + ')', curr.opened, curr.closed + 1))
    return result




















def main():
    print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))


main()

def circular_array_loop_exists2(arr):
    '''
    We are given an array containing positive and negative numbers.
    Suppose the array contains a number ‘M’ at a particular index.
    Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative
    move backwards ‘M’ indices. You should assume that the array is circular which means two things:
        1. If, while moving forward, we reach the end of the array,
            we will jump to the first element to continue the movement.
        2. If, while moving backward, we reach the beginning of the array,
            we will jump to the last element to continue the movement.

    Write a method to determine if the array has a cycle.

    The cycle should have more than one element and should follow one direction
    which means the cycle should not contain both forward and backward movements.
    '''

    for i in range(len(arr)):
        visited = [False for x in arr]
        sign = arr[i] > 0

        current_value = arr[i]
        current_index = i

        while True:
            if sign != (current_value > 0):
                break

            if visited[current_index] == True:
                return True

            visited[current_index] = True

            current_index = (current_index + current_value) % len(arr)
            current_value = arr[current_index]

    return False

def circular_array_loop_exists(arr):
    '''
    We are given an array containing positive and negative numbers.
    Suppose the array contains a number ‘M’ at a particular index.
    Now, if ‘M’ is positive we will move forward ‘M’ indices and if ‘M’ is negative
    move backwards ‘M’ indices. You should assume that the array is circular which means two things:
        1. If, while moving forward, we reach the end of the array,
            we will jump to the first element to continue the movement.
        2. If, while moving backward, we reach the beginning of the array,
            we will jump to the last element to continue the movement.

    Write a method to determine if the array has a cycle.

    The cycle should have more than one element and should follow one direction
    which means the cycle should not contain both forward and backward movements.
    '''
    for i in range(len(arr)):
        slow, fast = i, i
        is_forward = arr[slow] >= 0

        while True:
            slow = do_step(arr, slow, is_forward)
            fast = do_step(arr, fast, is_forward)

            if fast != -1:
                fast = do_step(arr, fast, is_forward)

            if slow == -1 or fast == -1 or slow == fast:
                break

        if slow != -1 and slow == fast:
            return True

    return False

def do_step(array, current_index, is_forward):
    step_size = array[current_index]
    next_index = (current_index + step_size) % len(array)

    if (array[next_index] > 0) != is_forward:
        return -1

    return next_index

def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))

main()
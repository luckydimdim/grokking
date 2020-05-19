def make_squares2(arr):
    '''
    Given a sorted array, create a new array containing
    squares of all the number of the input array in the sorted order.
    '''

    squares = []

    for el in arr:
        squares.append(abs(el * el))

    squares.sort()

    return squares

def make_squares3(arr):
    '''
    Given a sorted array, create a new array containing
    squares of all the number of the input array in the sorted order.
    '''

    left, right = 0, 0
    squares = []

    while arr[left] < 0:
        left += 1

    if arr[left + 1] != None:
        right = left + 1
    elif arr[left - 1] != None:
        right = left
        left -= 1

    while left >= 0 or right < len(arr):
        if left >= 0 and right < len(arr):
            left_sqr = arr[left] * arr[left]
            right_sqr = abs(arr[right] * arr[right])

            if left_sqr == right_sqr:
                squares.append(left_sqr)
                squares.append(right_sqr)
                left -= 1
                right += 1
            elif left_sqr < right_sqr:
                squares.append(left_sqr)
                left -= 1
            else:
                squares.append(right_sqr)
                right += 1
        elif left >= 0:
            squares.append(arr[left] * arr[left])
            left -= 1
        else:
            squares.append(abs(arr[right] * arr[right]))
            right += 1

    return squares

def make_squares(arr):
    '''
    Given a sorted array, create a new array containing
    squares of all the number of the input array in the sorted order.
    '''

    squares = [0 for x in range(len(arr))]
    pointer = len(arr) - 1
    left, right = 0, pointer

    while left <= right:
        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]

        if left_square > right_square:
            squares[pointer] = left_square
            left += 1
        else:
            squares[pointer] = right_square
            right -= 1

        pointer -= 1

    return squares

#                |
array = [-2, -1, 0, 2, 3]
#                |

print(make_squares(array))
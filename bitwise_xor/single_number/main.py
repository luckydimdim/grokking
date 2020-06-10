def find_single_number2(arr):
    '''
    In a non-empty array of integers, every number appears twice except for one, find that single number.
    '''
    x1 = 1 ^ 1
    for i in range(2, len(arr) // 2 + 2):
        x1 = x1 ^ i
        x1 = x1 ^ i

    x2 = arr[0]
    for i in range(1, len(arr)):
        x2 = x2 ^ arr[i]

    return x1 ^ x2

def find_single_number(arr):
    num = 0
    for i in arr:
        num ^= i
    return num

def main():
    arr = [1, 4, 2, 1, 3, 2, 3]
    print(find_single_number(arr))

main()
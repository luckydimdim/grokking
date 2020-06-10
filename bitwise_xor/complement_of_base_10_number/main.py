def calculate_bitwise_complement2(n):
    '''
    Every non-negative integer N has a binary representation, for example,
    8 can be represented as “1000” in binary and 7 as “0111” in binary.
    The complement of a binary representation is the number in binary
    that we get when we change every 1 to a 0 and every 0 to a 1.
    For example, the binary complement of “1010” is “0101”.
    For a given positive number N in base-10,
    return the complement of its binary representation as a base-10 integer.
    '''

    b = num_to_bin(n)
    converted = ''

    for digit in b:
        if digit == '1':
            converted += '0'
        else:
            converted += '1'

    n = bin_to_num(converted)

    return n

def num_to_bin(num):
    result = ''
    while num > 0:
        remainer = num % 2
        num //= 2
        if remainer == 0:
            result = '0'+ result
        else:
            result = '1'+ result

    return result

def bin_to_num(str):
    result = 0
    pointer = len(str) - 1
    counter = 0

    while pointer > 0:
        result += int(str[pointer]) * 2**counter
        counter += 1
        pointer -= 1

    return result

def calculate_bitwise_complement(num):
    bit_count, n = 0, num
    while n > 0:
        bit_count += 1
        n = n >> 1

    all_bits_set = pow(2, bit_count) - 1

    return num ^ all_bits_set

def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))

main()
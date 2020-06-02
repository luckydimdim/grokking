def find_letter_case_string_permutations2(str):
    '''
    Given a string, find all of its permutations preserving the character sequence but changing case.
    '''
    permutations = []
    permutations.append(str)

    for i in range(len(str)):
        if str[i].isalpha():
            n = len(permutations)
            for j in range(n):
                chs = list(permutations[j])
                chs[i] = chs[i].swapcase()
                permutations.append(''.join(chs))

    return permutations

def find_letter_case_string_permutations(str):
    '''
    Given a string, find all of its permutations preserving the character sequence but changing case.
    '''
    result = [str]

    for i in range(len(str)):
        if str[i].isalpha():
            cur_len = len(result)
            for j in range(cur_len):
                new = list(result[j])
                new[i] = new[i].swapcase()
                result.append(''.join(new))


    return result

def main():
    print("String permutations are: " +
            str(find_letter_case_string_permutations("ad52")))
    print("String permutations are: " +
            str(find_letter_case_string_permutations("ab7c")))


main()

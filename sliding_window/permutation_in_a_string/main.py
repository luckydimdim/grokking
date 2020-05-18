def find_permutation2(str, pattern):
    '''
    Given a string and a pattern, find out if the
    string contains any permutation of the pattern.
    '''

    perm = {}

    for letter in pattern:
        if letter not in perm:
            perm[letter] = 0
        perm[letter] += 1

    backup = perm.copy()

    for window_end in range(len(str)):
        if str[window_end] in perm and perm[str[window_end]] > 0:
            perm[str[window_end]] -= 1
            if sum(perm.values()) == 0:
                return True
        else:
            perm = backup.copy()

    return False

def find_permutation(str, pattern):
    '''
    Given a string and a pattern, find out if the
    string contains any permutation of the pattern.
    '''

    matched_counter, window_start = 0, 0
    char_frequency = {}

    for letter in pattern:
        if letter not in char_frequency:
            char_frequency[letter] = 0
        char_frequency[letter] += 1

    for window_end in range(len(str)):
        if str[window_end] in char_frequency:
            char_frequency[str[window_end]] -= 1
            if char_frequency[str[window_end]] == 0:
                matched_counter += 1

        if matched_counter == len(pattern):
            return True

        if window_end + 1 >= len(pattern):
            if str[window_start] in char_frequency:
                if char_frequency[str[window_start]] == 0:
                    matched_counter -= 1

                char_frequency[str[window_start]] += 1

            window_start += 1

    return False

#            |
string = 'aaacb'
pattern = 'abc'

print(find_permutation(string, pattern))
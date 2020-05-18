def find_substring(str, pattern):
    '''
    Given a string and a pattern, find the smallest substring
    in the given string which has all the characters of the given pattern.
    '''
    window_start, matches = 0, 0
    uniques = {}
    smallest_substring = ''

    for letter in pattern:
        if letter not in uniques:
            uniques[letter] = 0
        uniques[letter] += 1

    for window_end in range(len(str)):
        if str[window_end] in uniques:
            uniques[str[window_end]] -= 1

            if uniques[str[window_end]] == 0:
                matches += 1

        while matches == len(pattern):
            smallest_substring = str[window_start:window_end + 1]
            window_start += 1

            if str[window_start] in uniques:
                if uniques[str[window_start]] == 0:
                    matches -= 1

                uniques[str[window_start]] += 1

    return smallest_substring

string = 'adcad'
pattern = 'abc'

print(find_substring(string, pattern))
def find_string_anagrams(str, pattern):
    '''
    Given a string and a pattern, find all anagrams
    of the pattern in the given string.
    Write a function to return a list of starting
    indices of the anagrams of the pattern in the given string.
    '''

    result_indexes = []

    window_start, matches = 0, 0
    uniques = {}

    for letter in pattern:
        if letter not in uniques:
            uniques[letter] = 0

        uniques[letter] += 1

    for window_end in range(len(str)):
        if str[window_end] in uniques:
            uniques[str[window_end]] -= 1
            if uniques[str[window_end]] == 0:
                matches += 1

        if matches == len(pattern):
            result_indexes.append(window_start)

        if window_end - window_start + 1 >= len(pattern):
            if str[window_start] in uniques:
                if uniques[str[window_start]] == 0:
                    matches -= 1
                uniques[str[window_start]] += 1
            window_start += 1

    return result_indexes

string = 'abbcabc'
pattern = 'abc'

print(find_string_anagrams(string, pattern))
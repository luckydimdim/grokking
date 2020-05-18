def length_of_longest_substring(str, k):
    '''
    Given a string with lowercase letters only,
    if you are allowed to replace no more than ‘k’
    letters with any letter, find the length of the
    longest substring having the same letters after replacement.
    '''
    max_length, window_start = 0, 0
    uniques = {}
    max_repeating_letter = 0

    for window_end in range(len(str)):
        if str[window_end] not in uniques:
            uniques[str[window_end]] = 0

        uniques[str[window_end]] += 1
        max_repeating_letter = max(max_repeating_letter, uniques[str[window_end]])

        if window_end - window_start + 1 - max_repeating_letter > k:
            uniques[str[window_start]] -= 1
            window_start += 1

        max_length = max(max_length, window_end - window_start + 1)

    return max_length

#            |
string = "aabccbb"
#
k = 2

print(length_of_longest_substring(string, k))

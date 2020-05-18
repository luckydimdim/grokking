def non_repeat_substring2(str):
    '''
    Given a string, find the length of the
    longest substring which has no repeating characters.
    '''
    window_start, max_length = 0, 0
    uniques = {}

    for window_end in range(len(str)):
        if str[window_end] not in uniques:
            uniques[str[window_end]] = True
        else:
            window_start = window_end

    max_length = max(max_length, window_end - window_start + 1)

    return max_length

def non_repeat_substring(str):
    window_start, max_length = 0, 0
    uniques = {}

    for window_end in range(len(str)):
        if str[window_end] in uniques:
            window_start = max(window_start, uniques[str[window_end]] + 1)

        uniques[str[window_end]] = window_end
        max_length = max(max_length, window_end - window_start + 1)

    return max_length

#            |
string = "aabbcabcbb"
#            |
print(non_repeat_substring(string))
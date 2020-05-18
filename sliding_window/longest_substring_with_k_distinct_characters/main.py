def longest_substring_with_k_distinct(str, k):
    '''
    Given a string, find the length of the longest substring
    in it with no more than K distinct characters.
    '''
    window_start, window_end = 0, 0
    max_length = 0
    distincts = {}

    while window_end < len(str):
        if maybe_add_to_distincts(str[window_end], distincts, k) == True:
            window_end += 1
            max_length = max(max_length, window_end - window_start)
        else:
            if str[window_start] in distincts:
                distincts[str[window_start]] -= 1

                if distincts[str[window_start]] == 0:
                    del distincts[str[window_start]]

            window_start += 1

    return max_length

def maybe_add_to_distincts(element, distincts, limit):
    if len(distincts) == limit and element not in distincts:
        return False

    if len(distincts) == limit and element in distincts:
        distincts[element] += 1
        return True

    if len(distincts) < limit:
        if element not in distincts:
            distincts[element] = 0
        distincts[element] += 1
        return True

    return False

print(longest_substring_with_k_distinct('cbbebi', 3))
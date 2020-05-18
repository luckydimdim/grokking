def find_word_concatenation(str, words):
    '''
    Given a string and a list of words, find all the starting indices
    of substrings in the given string that are a concatenation
    of all the given words exactly once without any overlapping
    of words. It is given that all words are of the same length.
    '''
    if len(words) == 0 or len(words[0]) == 0:
        return []

    word_frequency = {}

    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    word_length = len(words[0])
    word_count = len(words)

    for i in range((len(str) - word_count * word_length)+1):
        words_seen = {}

        for j in range(word_count):
            next_word_index = i + j * word_length
            word = str[next_word_index: next_word_index + word_length]

            if word not in word_frequency:
                break

            if word not in words_seen:
                words_seen[word] = 0
            words_seen[word] += 1


            if words_seen[word] > word_frequency.get(word, 0):
                break

            if j + 1 == word_count:
                result_indices.append(i)

    return result_indices

string = 'catfoxcat'
words = ['cat', 'fox']

print(find_word_concatenation(string, words))
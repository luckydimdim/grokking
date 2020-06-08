from collections import deque

def generate_generalized_abbreviation2(word):
    '''
    Given a word, write a function to generate all of its unique generalized abbreviations.
    Generalized abbreviation of a word can be generated by replacing each substring
    of the word by the count of characters in the substring.
    Take the example of “ab” which has four substrings: “”, “a”, “b”, and “ab”.
    After replacing these substrings in the actual word by the count of characters
    we get all the generalized abbreviations: “ab”, “1b”, “a1”, and “2”.
    '''
    result = []
    queue = deque()
    queue.append('')

    for i in range(len(word) + 1):
        queue_size = len(queue)

        for _ in range(queue_size):
            curr = queue.popleft()

            if len(curr) == len(word):
                result.append(curr)
            else:
                queue.append(curr + word[i])
                queue.append(curr + '_')

    for i in range(len(result)):
        result[i] = bamba(result[i])

    return result

def bamba(word):
    left, right = 0, 0
    counter = 0
    result = word

    while right < len(word):
        if word[right] == '_':
            counter += 1
            ll = list(word)
            ll[left] = str(counter)
            result = ''.join(ll)
        else:
            counter = 0
            left = right + 1
        right += 1

    return result.replace('_', '')

class Word:
    def __init__(self, value, start, count):
        self.value = value
        self.start = start
        self.count = count

def generate_generalized_abbreviation3(input):
    word_len = len(input)
    result = []
    queue = deque()
    queue.append(Word(list(), 0, 0))
    while queue:
        word = queue.popleft()
        if word.start == word_len:
            if word.count != 0:
                word.value.append(str(word.count))
            result.append(''.join(word.value))
        else:
            queue.append(Word(word.value, word.start + 1, word.count + 1))
            if word.count != 0:
                word.value.append(str(word.count))

            new_word = list(word.value)
            new_word.append(input[word.start])
            queue.append(Word(new_word, word.start + 1, 0))

    return result

def generate_generalized_abbreviation(word):
    '''
    Given a word, write a function to generate all of its unique generalized abbreviations.
    Generalized abbreviation of a word can be generated by replacing each substring
    of the word by the count of characters in the substring.
    Take the example of “ab” which has four substrings: “”, “a”, “b”, and “ab”.
    After replacing these substrings in the actual word by the count of characters
    we get all the generalized abbreviations: “ab”, “1b”, “a1”, and “2”.
    '''
    result = []
    queue = deque()
    queue.append('')

    for i in range(len(word)):
        queue_size = len(queue)
        for _ in range(queue_size):
            curr = queue.popleft()
            queue.append(curr + '_')
            queue.append(curr + word[i])

    while queue:
        curr = queue.popleft()
        temp = ''
        cursor = 0
        counter = 0
        while cursor < len(curr):
            if curr[cursor] == '_':
                counter += 1
            else:
                if counter > 0:
                    temp += str(counter)
                temp += curr[cursor]
                counter = 0
            cursor += 1
        if counter > 0:
            temp += str(counter)
        result.append(temp)

    return result

def main():
    print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("BAT")))
    print("Generalized abbreviation are: " +
        str(generate_generalized_abbreviation("code")))

main()

def backspace_compare2(str1, str2):
    '''
    Given two strings containing backspaces
    (identified by the character ‘#’), check if the two strings are equal.
    '''

    return clear(str1) == clear(str2)

def clear(string):
    i = len(string) - 1
    while i >= 0:
        if string[i] == '#':
            string = string[:i] + string[i+1:]
            i -= 1

            j = i
            while string[j] == '#':
                j -= 1

            string = string[:j] + string[j+1:]
        i -= 1
    return string

def backspace_compare(str1, str2):
    '''
    Given two strings containing backspaces
    (identified by the character ‘#’), check if the two strings are equal.
    '''

    top, bottom = len(str1) - 1, len(str2) - 1

    while top >= 0 and bottom >= 0:
        if str1[top] == '#':
            skip = 0
            while str1[top] == '#':
                skip += 1
                top -= 1
            top -= skip

        if str2[bottom] == '#':
            skip = 0
            while str2[bottom] == '#':
                skip += 1
                bottom -= 1
            bottom -= skip

        if str1[top] != str2[bottom]:
            return False

        top -= 1
        bottom -= 1

    return True

str1 = "xy#z"
str2 = "xyz#"

print(backspace_compare(str1, str2))
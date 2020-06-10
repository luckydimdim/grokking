def flip_and_invert_image(matrix):
    '''
    Given a binary matrix representing an image,
    we want to flip the image horizontally, then invert it.
    To flip an image horizontally means that each row of the image is reversed.
    For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].
    To invert an image means that each 0 is replaced by 1,
    and each 1 is replaced by 0.
    For example, inverting [1, 1, 0] results in [0, 0, 1].
    '''
    for row in matrix:
        index = 0
        while index < len(row) // 2:
            row[index], row[len(row) - index - 1] = row[len(row) - index - 1], row[index]
            index += 1

        for i in range(len(row)):
            row[i] ^= 1

    return matrix


def main():
    print(flip_and_invert_image([[1,0,1], [1,1,1], [0,1,1]]))
    print(flip_and_invert_image([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))

main()
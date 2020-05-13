def fruits_into_baskets(fruits):
    '''
    Given an array of characters where each character represents a fruit tree,
    you are given two baskets and your goal is to put maximum number of fruits in each basket.

    The only restriction is that each basket can have only one type of fruit.
    You can start with any tree, but once you have started you can’t skip a tree.

    You will pick one fruit from each tree until you cannot,
    i.e., you will stop when you have to pick from a third fruit type.
    Write a function to return the maximum number of fruits in both the baskets.
    '''
    window_start, max_value = 0, 0
    baskets = {}

    for window_end in range(len(fruits)):
        if fruits[window_end] not in baskets:
            baskets[fruits[window_end]] = 0

        baskets[fruits[window_end]] += 1

        if len(baskets) == 2:
            max_value = max(max_value, sum(baskets.values()))

        while len(baskets) == 3:
            baskets[fruits[window_start]] -= 1

            if baskets[fruits[window_start]] == 0:
                del baskets[fruits[window_start]]

            window_start += 1

    return max_value

fruits = ['A', 'B', 'C', 'A', 'C']
print(fruits_into_baskets(fruits))
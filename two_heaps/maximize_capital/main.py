from heapq import *

def find_maximum_capital2(capitals, profits, number_of_projects, initial_capital):
    '''
    Given a set of investment projects with their respective profits,
    we need to find the most profitable projects. We are given an initial capital and are allowed
    to invest only in a fixed number of projects. Our goal is to choose projects that give us
    the maximum profit.
    We can start an investment project only when we have the required capital. Once a project is selected,
    we can assume that its profit has become our capital.
    '''
    capitals.sort()
    profits.sort()
    result = [initial_capital]
    capital = None
    while number_of_projects > 0:
        if capital is None:
            capital = initial_capital

        pointer = 0
        max_capital = 0
        for i in range(len(capitals)):
            if capitals[i] <= capital:
                max_capital = max(max_capital, capitals[pointer])
                pointer = i

        profit = profits[pointer]
        result.append(profit)
        capital += profit

        number_of_projects -= 1

    return sum(result)

def find_maximum_capital(capitals, profits, number_of_projects, initial_capital):
    '''
    Given a set of investment projects with their respective profits,
    we need to find the most profitable projects. We are given an initial capital and are allowed
    to invest only in a fixed number of projects. Our goal is to choose projects that give us
    the maximum profit.
    We can start an investment project only when we have the required capital. Once a project is selected,
    we can assume that its profit has become our capital.
    '''
    min_cap_heap, max_prof_heap = [], []
    for i in capitals:
        heappush(min_cap_heap, (capitals[i], i))

    capital = initial_capital
    for _ in range(number_of_projects):
        while min_cap_heap and min_cap_heap[0][0] <= capital:
            cur_capital, i = heappop(min_cap_heap)
            heappush(max_prof_heap, (-profits[i], i))

        if not max_prof_heap:
            break

        capital += -heappop(max_prof_heap)[0]

    return capital

def main():
    print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))

main()

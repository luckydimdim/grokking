def search_quadruplets2(arr, target):
    '''
    Given an array of unsorted numbers and a target number,
    find all unique quadruplets in it, whose sum is equal to the target number.
    '''
    quadruplets = []
    first = 0

    arr.sort()

    while first < len(arr) - 3:
        second = first + 1

        while second < len(arr) - 2:
            left = second + 1
            right = len(arr) - 1

            while left < right:
                current_sum = arr[first] + arr[second] + arr[left] + arr[right]

                if current_sum > target:
                    right -= 1
                    continue

                if current_sum < target:
                    left += 1
                    continue

                if right != len(arr) - 1 and arr[right] == arr[right + 1]:
                    right -= 1
                    continue

                quadruplet = [arr[first], arr[second], arr[left], arr[right]]
                quadruplets += [quadruplet]
                right -= 1

            second += 1

        first += 1

    return quadruplets

def search_quadruplets(arr, target):
    '''
    Given an array of unsorted numbers and a target number,
    find all unique quadruplets in it, whose sum is equal to the target number.
    '''
    quadruplets = []
    arr.sort()

    for i in range(len(arr)-3):
        if i > 0 and arr[i] == arr[i - 1]:
            continue

        for j in range(i + 1, len(arr)-2):
            if j > i + 1 and arr[j] == arr[j - 1]:
                continue

            search_pairs(arr, target, i, j, quadruplets)

    return quadruplets

def search_pairs(arr, target_sum, first, second, quadruplets):
    left = second + 1
    right = len(arr) - 1

    while left < right:
        current_sum = arr[first] + arr[second] + arr[left] + arr[right]
        if current_sum == target_sum:
            quadruplets.append([arr[first], arr[second], arr[left], arr[right]])
            left += 1
            right -= 1

            while left < right and arr[left] == arr[left - 1]:
                left += 1

            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1

arr, target = [2, 0, -1, 1, -2, 2], 2
#arr, target = [4, 1, 2, -1, 1, -3], 1

print(search_quadruplets(arr, target))
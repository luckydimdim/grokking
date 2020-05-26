def find_first_k_missing_positive(nums, k):
    '''
    Given an unsorted array containing numbers and a number ‘k’,
    find the first ‘k’ missing positive numbers in the array.
    '''
    i, n = 0, len(nums)

    while i < n:
        j = nums[i] - 1
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
        else:
            i += 1

    missing_numbers = []
    extra_numbers = set()
    for i in range(n):
        if len(missing_numbers) < k:
            if nums[i] != i + 1:
                missing_numbers.append(i + 1)
                extra_numbers.add(nums[i])

    counter = 1
    while len(missing_numbers) < k:
        candidate = n + counter
        if candidate not in extra_numbers:
            missing_numbers.append(candidate)
        counter += 1

    return missing_numbers

nums, k = [2, 3, 4], 3

print(find_first_k_missing_positive(nums, k))
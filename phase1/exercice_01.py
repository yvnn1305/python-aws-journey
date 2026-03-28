def filter_and_sort(nums):
    pairs = [x for x in nums if x % 2 == 0]
    pairs.sort(reverse = True)
    return pairs

print(filter_and_sort([4, 1, 3, 2, 5, 23, 42, 12]))

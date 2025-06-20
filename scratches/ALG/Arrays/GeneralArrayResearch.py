def generalResearch(arr, m):
    if len(arr) == 1:
        if arr[0] == m:
            return 1
        else:
            return 0

    median = len(arr) // 2
    left = arr[:median]
    right = arr[median:]

    return generalResearch(left, m) + generalResearch(right, m)


nums = [1, 2, 4, 6, 6]
print(generalResearch(nums, 6))
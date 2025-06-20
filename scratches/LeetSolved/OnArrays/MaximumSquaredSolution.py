def find_cardinality(num,  nums_set):
    cardinality = 1
    current = num
    while current * current in nums_set:
        current = current * current
        cardinality += 1
    return cardinality

def maximum_squared_subset(nums):
    nums_set = set(nums)
    max_cardinality = 0

    for num in nums_set:
        cardinality = find_cardinality(num, nums_set)
        if cardinality > max_cardinality:
            max_cardinality = cardinality

    return max_cardinality

arr = [1, 2 ,3 ,4 ,5 ,5 ,5, 5, 6, 6, 1, 1, 1, 1, 1, 1, 1]

print(maximum_squared_subset(arr))

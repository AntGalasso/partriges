def find_cardinality(num, doubles, nums):
    doubles.remove(num)
    if (num * num) is not nums:
        return 1
    else:
        return 2 + find_cardinality(num, doubles)


def maximum_squared_subset(nums):
    seen = set()
    doubles = set()
    max_cardinality = 0
    surplus = 0

    nums = sorted(nums)
    count_ones = nums.count(1)

    if count_ones == 1:
        max_cardinality = count_ones
    if count_ones % 2 == 1:
        surplus = count_ones - 1
        max_cardinality = count_ones
    else:
        max_cardinality = count_ones - 1
        surplus = count_ones


    for num in nums:
        if num in seen:
            doubles.add(num)
        else:
            seen.add(num)

    while doubles:
        for n in doubles:
            cardinality = find_cardinality(n, doubles, nums)
            if (cardinality + surplus) > max_cardinality:
                max_cardinality = (cardinality + surplus)
    return max_cardinality

nums = [1, 0, 1, 1, 0, 1]
print(maximum_squared_subset(nums))


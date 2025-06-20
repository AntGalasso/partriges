"""
def limSup(arr, m, i, j):

    if i > j:
        return -1
    if arr[i] == m:
        return i
    if i == j-1:
        return j

    median = (i+j) // 2

    if arr[median] > m:
        return limSup(arr, m, i+1, median)
    else:
        return limSup(arr, m, median-1, j)

"""
def limSup(arr, m, i, j):
    if i > j:
        return -1
    if arr[i] == m:
        return i
    if i == j - 1:
        if arr[j] > m:
            return j
        else:
            return -1

    median = (i + j) // 2

    if arr[median] > m:
        return limSup(arr, m, i + 1, median)
    else:
        return limSup(arr, m, median + 1, j)



nums = [1, 2, 5, 5, 6]

print(limSup(nums, 3, 0, len(nums)))
# input: arr, n
# output: result = [] on pairs such that (u + v) >= k

def maxValidPairs(arr, k):
    i = 0
    j = len(arr)
    used = [False] * j
    result = []

    arr = sorted(arr)
    while i < j:

        if arr[i] + arr[j] >= k:
            result.append(arr[i], arr[j])

            j -= 1
            i += 1

            used[i] = used[j] = True
        else:
            i += 1

    return result


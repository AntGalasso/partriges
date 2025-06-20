def myBinaryResearch(arr, k, start, end):
    if start > end:
        return -1

    median = (start + end) // 2
    if k == arr[median]:
        return median
    if k < arr[median]:
        return myBinaryResearch(arr, k, start, median - 1)
    else:
        return myBinaryResearch(arr, k, median + 1, end)


def contaPromossi(arr, k, start, end):
    firstPromoted = myBinaryResearch(arr, k, start, end)
    return len(arr[firstPromoted:])

def contaPromossi2(arr, k, start, end):
    if start > end:
        return 0
    m = (start + end) // 2
    if arr[m] <= k:
        #vado a destra e non conto
        return contaPromossi2(arr, k, m + 1, end)
    else:
        return (end - (m + 1)) + contaPromossi2(arr, k, start, m - 1)


#promossi non funziona se k != nums[i] for each i


nums = [1, 4, 5, 6, 6]
print("ricerca binaria ha dato indice:")
print(myBinaryResearch(nums, 5, 0, len(nums) - 1))

print("promossi: ")
print(contaPromossi2(nums, 0, 0, len(nums) - 1))

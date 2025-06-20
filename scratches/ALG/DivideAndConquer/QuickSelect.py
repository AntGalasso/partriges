def quickSelect(arr, k):
    rango = k - 1

    if len(arr) == 1:
        return arr[0]
    pivot = arr[len(arr)//2]
    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if rango < len(lows):
        return quickSelect(lows, k)
    elif rango < len(lows) + len(pivots):
        return pivot
    else:
        return quickSelect(highs, k - len(lows) - len(pivots))

arr = [7, 2, 9, 1, 5, 8, 3, 4 , 6]
print(quickSelect(arr, 5))




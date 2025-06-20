def permuta(array, k):
    if k == len(array):
        print(array)
    else:
        for i in range (k, len(array)):
            array[i], array[k] = array[k], array[i]
            permuta(array, k+1)
            array[i], array[k] = array[k], array[i]



arr = [1, 2, 3]
permuta(arr, 0)




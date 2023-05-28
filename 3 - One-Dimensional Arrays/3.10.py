def cyclic(arr, k):
    k = k % len(arr)

    temp = arr[-k:]
    arr[k:] = arr[:-k]
    arr[:k] = temp

    return arr

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

k = 3
shiftedArr = cyclic(array, k)
print(shiftedArr)

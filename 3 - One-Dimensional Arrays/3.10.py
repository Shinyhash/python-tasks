def cyclic_shift_right(arr, k):
    k = k % len(arr)

    temp = arr[-k:]
    arr[k:] = arr[:-k]
    arr[:k] = temp

    return arr

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
shifted_array = cyclic_shift_right(array, k)
print(shifted_array)

def cyclic_shift_left(arr, k):
    k = k % len(arr)

    temp = arr[:k]
    arr[:len(arr)-k] = arr[k:]
    arr[len(arr)-k:] = temp

    return arr

# Пример использования:
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
shifted_array = cyclic_shift_left(array, k)
print(shifted_array)

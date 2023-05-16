arr = [1, 2, 3, 4, 5]

def transform_array(arr):
    last_elem = arr[-1]
    for i in range(1, len(arr) - 1):
        if arr[i] % 2 != 0:
            arr[i] += last_elem
    return arr

transformed_arr = transform_array(arr)
print(transformed_arr)

original_array = [3, 7, 4, 6, 2, 9, 5]

def transform_array(arr):
    if len(arr) <= 2:
        return arr

    first_element = arr[0]

    for i in range(1, len(arr)-1):
        if arr[i] % 2 == 0:
            arr[i] += first_element

    return arr

transformed_array = transform_array(original_array)
print(transformed_array)

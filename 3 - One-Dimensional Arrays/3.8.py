def reverse_elements_between_min_max(arr):
    min_index = arr.index(min(arr))
    max_index = arr.index(max(arr))

    if min_index > max_index:
        min_index, max_index = max_index, min_index

    reversed_elements = arr[:min_index] + arr[max_index:min_index:-1] + arr[max_index+1:]

    return reversed_elements

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
reversed_array = reverse_elements_between_min_max(array)
print(reversed_array)

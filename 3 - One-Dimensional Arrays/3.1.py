def get_even_elements(arr):
    even_arr = []
    for i in arr:
        if i % 2 == 0:
            even_arr.append(i)
    return even_arr
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
even_arr = get_even_elements(arr)
print(even_arr)
def filter_array_by_multiples(arr, n):
    result = []
    for num in arr:
        if num % n == 0:
            result.append(num)
    return result

# Пример использования
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
multiple = 3
filtered_array = filter_array_by_multiples(array, multiple)
print(filtered_array)

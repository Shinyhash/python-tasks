def filter(arr, n):
    result = []
    for num in arr:
        if num % n == 0:
            result.append(num)
    return result

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

multiple = 3
filteredArr = filter(array, multiple)
print(filteredArr)

def filter_array(arr, k):
    result = []
    for num in arr:
        if str(num).startswith(str(k)):
            result.append(num)
    return result
arr = [123, 45, 678, 90, 234]
k = 2
result = filter_array(arr, k)
print(result)
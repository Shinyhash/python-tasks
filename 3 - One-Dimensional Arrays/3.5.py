arr = [1, 2, 3, 4, 5]

def transform(arr):
    lastE = arr[-1]
    for i in range(1, len(arr) - 1):
        if arr[i] % 2 != 0:
            arr[i] += lastE
    return arr

transformedArr = transform(arr)
print(transformedArr)

Array = [3, 7, 4, 6, 2, 9, 5]

def transform(arr):
    if len(arr) <= 2:
        return arr

    firstE = arr[0]

    for i in range(1, len(arr)-1):
        if arr[i] % 2 == 0:
            arr[i] += firstE

    return arr

transformedArr = transform(Array)
print(transformedArr)

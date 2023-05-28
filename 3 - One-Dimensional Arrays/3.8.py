def reverse(arr):
    minI = arr.index(min(arr))
    maxI = arr.index(max(arr))

    if minI > maxI:
        minI, maxI = maxI, minI

    reversedE = arr[:minI] + arr[maxI:minI:-1] + arr[maxI+1:]

    return reversedE

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

reversedArr = reverse(array)
print(reversedArr)

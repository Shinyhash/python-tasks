def getEven(arr):
    evenArr = []
    for i in arr:
        if i % 2 == 0:
            evenArr.append(i)
    return evenArr

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

evenArr = getEven(arr)
print(evenArr)
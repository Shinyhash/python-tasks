arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

newArr = []

for i in arr:
    if i % 2 != 0:
        newArr.append(i)

print(newArr)
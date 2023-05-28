R = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10, 11, 12]]

newR = [[element * 5 for element in row] for row in R]

sumFr = sum(newR[0])

for row in newR:
    print("|", end="")
    for element in row:
        print(f" {element:3} |", end="")
    print()

print(f"Сумма значений элементов первой строки нового массива: {sumFr}")

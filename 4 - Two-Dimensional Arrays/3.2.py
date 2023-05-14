R = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [10, 11, 12]]

new_R = [[element * 5 for element in row] for row in R]

sum_first_row = sum(new_R[0])

for row in new_R:
    print("|", end="")
    for element in row:
        print(f" {element:3} |", end="")
    print()

print(f"Сумма значений элементов первой строки нового массива: {sum_first_row}")

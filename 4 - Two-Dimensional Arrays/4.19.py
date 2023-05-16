matrix = [
    [3, 2, 6, 7, 8, 5, 9, 1, 4, 2],
    [5, 4, 3, 8, 9, 1, 7, 6, 2, 4],
    [8, 6, 9, 2, 3, 4, 1, 7, 5, 9],
    [2, 1, 5, 3, 4, 6, 8, 9, 7, 1],
    [9, 7, 4, 5, 1, 2, 3, 6, 8, 7]
]

min_element = matrix[0][0]
min_row_index = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] < min_element:
            min_element = matrix[i][j]
            min_row_index = i

del matrix[min_row_index]

for row in matrix:
    print(row)

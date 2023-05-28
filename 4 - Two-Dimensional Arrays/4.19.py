matrix = [
    [3, 2, 6, 7, 8, 5, 9, 1, 4, 2],
    [5, 4, 3, 8, 9, 1, 7, 6, 2, 4],
    [8, 6, 9, 2, 3, 4, 1, 7, 5, 9],
    [2, 1, 5, 3, 4, 6, 8, 9, 7, 1],
    [9, 7, 4, 5, 1, 2, 3, 6, 8, 7]
]

minE = matrix[0][0]
minI = 0
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        if matrix[i][j] < minE:
            minE = matrix[i][j]
            minI = i

del matrix[minI]

for row in matrix:
    print(row)

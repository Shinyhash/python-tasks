matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

maxE = matrix[0][0]
maxI = 0
maxJ = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > maxE:
            maxE = matrix[i][j]
            maxI = i
            maxJ= j

for i in range(len(matrix)):
    matrix[i][maxJ], matrix[maxI][i] = matrix[maxI][i], matrix[i][maxJ]

for row in matrix:
    print(row)
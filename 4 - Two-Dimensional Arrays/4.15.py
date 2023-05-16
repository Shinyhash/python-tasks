matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

max_elem = matrix[0][0]
max_i = 0
max_j = 0
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if matrix[i][j] > max_elem:
            max_elem = matrix[i][j]
            max_i = i
            max_j = j

for i in range(len(matrix)):
    matrix[i][max_j], matrix[max_i][i] = matrix[max_i][i], matrix[i][max_j]

for row in matrix:
    print(row)

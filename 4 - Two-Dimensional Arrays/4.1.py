matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = -matrix[i][j]

for row in matrix:
    print("|", end="")
    for item in row:
        print(f" {item:3} |", end="")
    print()

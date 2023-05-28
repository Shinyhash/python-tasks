def swap_rows(matrix, k, j):
    temp = matrix[k]
    matrix[k] = matrix[j]
    matrix[j] = temp
    return matrix
    
N = 4
matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

k = 1
j = 3

result = swap_rows(matrix, k, j)

for row in result:
    print(row)

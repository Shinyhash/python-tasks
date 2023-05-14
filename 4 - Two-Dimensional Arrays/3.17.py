matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

for i in range(len(matrix)):
    max_in_row = max(matrix[i])
    column_index = matrix[i].index(max_in_row)
    column = [row[column_index] for row in matrix]
    if max_in_row == min(column):
        print(max_in_row)
        break
else:
    print(0)

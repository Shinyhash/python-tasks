matrix = [
    [1, 0, 2, 0],
    [0, 0, 0, 0],
    [3, 0, 4, 0],
    [0, 0, 0, 0]
]

def remove_zero_columns(matrix):
    new_matrix = []
    for column in range(len(matrix[0])):
        column_has_value = False
        for row in range(len(matrix)):
            if matrix[row][column] != 0:
                column_has_value = True
                break
        if column_has_value:
            new_matrix.append([matrix[row][column] for row in range(len(matrix))])
    return new_matrix

new_matrix = remove_zero_columns(matrix)
print(new_matrix)

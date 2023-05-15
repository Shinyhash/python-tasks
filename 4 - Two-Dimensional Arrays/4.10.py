matrix = [
    [1.0, 2.0, 3.0],
    [4.0, 5.0, 6.0],
    [7.0, 8.0, 9.0],
]

def find_row_diffs(matrix):
    n, m = len(matrix), len(matrix[0])
    diffs = [0] * n  # инициализируем массив нулями

    for i in range(n):
        row_min, row_max = float('inf'), float('-inf')
        for j in range(m):
            row_min = min(row_min, matrix[i][j])
            row_max = max(row_max, matrix[i][j])
        diffs[i] = row_max - row_min

    return diffs

diffs = find_row_diffs(matrix)
print(diffs)

matrix = [
    [1, 2, 3],
    [0, 0, 0],
    [4, 5, 6],
    [0, 0, 0]
]

def find_zero_rows(matrix):
    n = len(matrix)
    zero_rows = []
    for i in range(n):
        if all(x == 0 for x in matrix[i]):
            zero_rows.append(i)
    return zero_rows

zero_rows = find_zero_rows(matrix)
print(zero_rows)

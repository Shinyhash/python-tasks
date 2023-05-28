matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

for i in range(len(matrix)):
    maxR = max(matrix[i])
    columnI = matrix[i].index(maxR)
    column = [row[columnI] for row in matrix]
    if maxR == min(column):
        print(maxR)
        break
else:
    print(0)

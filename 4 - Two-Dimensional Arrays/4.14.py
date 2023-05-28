matrix = [
    [1, 0, 2, 0],
    [0, 0, 0, 0],
    [3, 0, 4, 0],
    [0, 0, 0, 0]
]

def removeCol(matrix):
    newM = []
    for column in range(len(matrix[0])):
        columnV = False
        for row in range(len(matrix)):
            if matrix[row][column] != 0:
                columnV = True
                break
        if columnV:
            newM.append([matrix[row][column] for row in range(len(matrix))])
    return newM

newM = removeCol(matrix)
print(newM)

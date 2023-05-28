matrix = [
    [1, 2, 3],
    [0, 0, 0],
    [4, 5, 6],
    [0, 0, 0]
]

def findR(matrix):
    n = len(matrix)
    zeroR = []
    for i in range(n):
        if all(x == 0 for x in matrix[i]):
            zeroR.append(i)
    return zeroR

zeroRm = findR(matrix)
print(zeroR)

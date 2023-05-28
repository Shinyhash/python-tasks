matrix = [
    [1, -2, 3, -4],
    [5, 6, -7, 8],
    [-9, 10, 11, -12]
]

b = []

for row in matrix:
    negativeC = sum(1 for elem in row if elem < 0)
    b.append(negativeC)

print(b)

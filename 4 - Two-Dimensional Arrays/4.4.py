B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

maxE = B[0][0]
maxT = 0
maxC = 0
for i in range(len(B)):
    for j in range(len(B[i])):
        if B[i][j] > maxE:
            maxE = B[i][j]
            maxR = i
            maxC = j

B[0][0], B[maxR][maxC] = B[maxR][maxC], B[0][0]

for row in B:
    print(row)

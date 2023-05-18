B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

max_element = B[0][0]
max_row = 0
max_col = 0
for i in range(len(B)):
    for j in range(len(B[i])):
        if B[i][j] > max_element:
            max_element = B[i][j]
            max_row = i
            max_col = j

B[0][0], B[max_row][max_col] = B[max_row][max_col], B[0][0]

for row in B:
    print(row)

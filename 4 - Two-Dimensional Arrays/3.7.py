matrix = [[4, 7, 3, 9, 5, 2, 1, 8, 6, 0],
          [9, 2, 6, 3, 1, 5, 7, 8, 0, 4],
          [1, 0, 3, 8, 5, 2, 4, 9, 7, 6],
          [8, 4, 2, 5, 3, 1, 6, 0, 9, 7],
          [0, 5, 3, 2, 1, 9, 7, 4, 6, 8]]

for row in matrix:
    min_elem = min(row)
    max_elem = max(row)

    min_index = row.index(min_elem)
    max_index = row.index(max_elem)

    row[min_index], row[max_index] = row[max_index], row[min_index]

for row in matrix:
    print(row)

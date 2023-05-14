matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

# Проходим по каждому элементу и меняем знак на противоположный
for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = -matrix[i][j]

# Выводим на экран новую матрицу в виде таблицы
for row in matrix:
    print("|", end="")
    for item in row:
        print(f" {item:3} |", end="")
    print()

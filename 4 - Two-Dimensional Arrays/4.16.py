import random

N = int(input("Введите размерность матрицы: "))

matrix = [[random.randint(0, 9) for j in range(N)] for i in range(N)]

print("Исходная матрица:")
for i in range(N):
    for j in range(N):
        print(matrix[i][j], end=" ")
    print()

k = int(input("Введите номер первой строки: "))
j = int(input("Введите номер второй строки: "))

temp = matrix[k]
matrix[k] = matrix[j]
matrix[j] = temp

print("Измененная матрица:")
for i in range(N):
    for j in range(N):
        print(matrix[i][j], end=" ")
    print()

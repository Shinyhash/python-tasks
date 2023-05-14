import random

m = int(input("количество строк (m) : "))
n = int(input("количество колонок (n) : "))

matr = [[random.randint(0, 10) for j in range(n)] for i in range(m)]

for i in range(m):
    for j in range(n):
        print(matr[i][j], end="\t")
    print()

count = 0
for i in range(m):
    stop = False
    for j in range(n-1):
        for k in range(j+1, n):
            if matr[i][j] == matr[i][k]:
                stop = True
                break
        if stop:
            break
    if not stop:
        count += 1

print("количество уникальных строк : ", count)

import random

random.seed()
M = 6
N = 8

mas = [[random.randint(0, 9) for i in range(N)] for j in range(M)]

for j in range(M):
    for i in range(N):
        print(mas[j][i], end=" ")
    print()

response = 0
t = 0
temp = 0
count = 0
totalC = 0

for z in range(N):
    for j in range(M):
        temp = mas[j][z]
        index = j
        for k in range(index + 1, M):
            if temp == mas[index+1][z]:
                count += 1
                index += 1
        if response < count:
            response = count + 1
        count = 0
        if totalC <= response:
            totalC = response
            t = z
        response = 0

print("Response:", totalC)
print("Column number:", t+1)

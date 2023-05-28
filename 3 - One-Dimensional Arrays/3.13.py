def negatives(R):
    S = []
    negativeC = 0

    for i in range(len(R)):
        if R[i] < 0:
            negativeC += 1
        S.append(R[i] * 2)

    return S, negativeC

R = [1, -2, 3, -4, 5, 6, -7, 8]

S, negativeC = negatives(R)
print("Количество отрицательных элементов в массиве R:", negativeC)
print("Массив S с увеличенными в два раза элементами R:", S)

def negativesR(R):
    countE = 0

    for i in range(len(R)):
        if R[i] % 2 == 0:
            countE += 1

        if R[i] < 0:
            R[i] = 111

    return countE, R

R = [10, -5, 8, 15, -20, 0, 7, -4, 12, -3]

countE, modifiedR = negativesR(R)
print("Количество элементов массива R, значения которых кратны 2:", countE)
print("Измененный массив R:", modifiedR)

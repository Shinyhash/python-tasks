def calculate(D):
    sumR = 0

    for i in range(len(D)):
        if -10 < D[i] < 20:
            sumR += D[i]

        if D[i] < 0:
            D[i] = 100

    return sumR, D

D = [15, 10, -5, 25, 0, -15, 30, 5, 12, -8]

sumR, modifiedD = calculate(D)
print("Сумма значений элементов, удовлетворяющих условию:", sumR)
print("Измененный массив D:", modifiedD)

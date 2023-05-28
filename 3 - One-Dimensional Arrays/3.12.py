def calculate(F):
    sumR = 0
    count33 = 0

    for i in range(len(F)):
        if F[i] != 33:
            sumR += F[i]
        else:
            count33 += 1

    return sumR, count33

F = [15, 33, 10, 25, 33, 0, 33, 5, 12, 33]

sumR, count33 = calculate(F)
print("Сумма элементов массива F, значения которых не равны 33:", sumR)
print("Количество элементов массива F, значения которых равны 33:", count33)

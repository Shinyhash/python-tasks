def calculate(A):
    sumOdd = 0
    countOdd = 0

    for i in range(len(A)):
        if i % 2 != 0:
            sumOdd += A[i]
            countOdd += 1

    averageOdd = round(sumOdd / countOdd, 2)

    for i in range(len(A)):
        if A[i] % 3 == 0:
            A[i] = averageOdd

    return averageOdd, A

A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]

averageOdd, modifiedA = calculate(A)
print("Среднее арифметическое значений элементов на нечетных местах:", averageOdd)
print("Измененный массив A:", modifiedA)

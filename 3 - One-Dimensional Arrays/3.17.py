def calculate_average_and_replace_multiple_of_3(A):
    sum_odd = 0
    count_odd = 0

    for i in range(len(A)):
        if i % 2 != 0:
            sum_odd += A[i]
            count_odd += 1

    average_odd = round(sum_odd / count_odd, 2)

    for i in range(len(A)):
        if A[i] % 3 == 0:
            A[i] = average_odd

    return average_odd, A

A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
average_odd, modified_A = calculate_average_and_replace_multiple_of_3(A)
print("Среднее арифметическое значений элементов на нечетных местах:", average_odd)
print("Измененный массив A:", modified_A)

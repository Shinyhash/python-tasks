def calculate_sum_and_count(F):
    sum_result = 0
    count_33 = 0

    for i in range(len(F)):
        if F[i] != 33:
            sum_result += F[i]
        else:
            count_33 += 1

    return sum_result, count_33

F = [15, 33, 10, 25, 33, 0, 33, 5, 12, 33]
sum_result, count_33 = calculate_sum_and_count(F)
print("Сумма элементов массива F, значения которых не равны 33:", sum_result)
print("Количество элементов массива F, значения которых равны 33:", count_33)

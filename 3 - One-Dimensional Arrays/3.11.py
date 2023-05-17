def calculate_sum_and_replace_elements(D):
    sum_result = 0

    for i in range(len(D)):
        if -10 < D[i] < 20:
            sum_result += D[i]

        if D[i] < 0:
            D[i] = 100

    return sum_result, D

D = [15, 10, -5, 25, 0, -15, 30, 5, 12, -8]
sum_result, modified_D = calculate_sum_and_replace_elements(D)
print("Сумма значений элементов, удовлетворяющих условию:", sum_result)
print("Измененный массив D:", modified_D)

def find_index_and_calculate_sum(K):
    index = -1
    sum_before_100 = 0

    for i in range(len(K)):
        if K[i] == 100:
            index = i
            break

    if index == -1:
        print("Элемент со значением 100 не найден.")
    else:
        for i in range(index):
            sum_before_100 += K[i]

    return index, sum_before_100

K = [10, 20, 30, 40, 50, 100, 60, 70, 80, 90, 100, 110]
index, sum_before_100 = find_index_and_calculate_sum(K)
print("Порядковый номер элемента со значением 100:", index)
print("Сумма значений элементов перед элементом со значением 100:", sum_before_100)

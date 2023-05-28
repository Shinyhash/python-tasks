def calculate(K):
    index = -1
    sumBefore = 0

    for i in range(len(K)):
        if K[i] == 100:
            index = i
            break

    if index == -1:
        print("Элемент со значением 100 не найден.")
    else:
        for i in range(index):
            sumBefore += K[i]

    return index, sumBefore

K = [10, 20, 30, 40, 50, 100, 60, 70, 80, 90, 100, 110]

index, sumBefore = calculate(K)
print("Порядковый номер элемента со значением 100:", index)
print("Сумма значений элементов перед элементом со значением 100:", sumBefore)

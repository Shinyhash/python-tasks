def double_elements_and_count_negatives(R):
    S = []
    negative_count = 0

    for i in range(len(R)):
        if R[i] < 0:
            negative_count += 1
        S.append(R[i] * 2)

    return S, negative_count

R = [1, -2, 3, -4, 5, 6, -7, 8]
S, negative_count = double_elements_and_count_negatives(R)
print("Количество отрицательных элементов в массиве R:", negative_count)
print("Массив S с увеличенными в два раза элементами R:", S)

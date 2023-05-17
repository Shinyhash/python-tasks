def count_even_and_replace_negatives(R):
    count_even = 0

    for i in range(len(R)):
        if R[i] % 2 == 0:
            count_even += 1

        if R[i] < 0:
            R[i] = 111

    return count_even, R

R = [10, -5, 8, 15, -20, 0, 7, -4, 12, -3]
count_even, modified_R = count_even_and_replace_negatives(R)
print("Количество элементов массива R, значения которых кратны 2:", count_even)
print("Измененный массив R:", modified_R)

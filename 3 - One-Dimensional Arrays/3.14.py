def swap_element_with_first(A):
    index = -1

    for i in range(len(A)):
        if A[i] == 49:
            index = i
            break

    if index == -1:
        print("Элемент со значением 49 не найден.")
    else:
        A[0], A[index] = A[index], A[0]

    return A

A = [10, 20, 30, 49, 40, 50, 60]
modified_A = swap_element_with_first(A)
print("Измененный массив A:", modified_A)

def rearrange_array(A):
    index = 0

    for i in range(len(A)):
        if A[i] < 0:
            A[i], A[index] = A[index], A[i]
            index += 1

    return A

A = [1, -2, 3, -4, 5, -6, 7, -8]
rearranged_A = rearrange_array(A)
print("Перемещенный массив A:", rearranged_A)

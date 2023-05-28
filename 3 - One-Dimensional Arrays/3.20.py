def swap(A):
    index = 0

    for i in range(len(A)):
        if A[i] < 0:
            A[i], A[index] = A[index], A[i]
            index += 1

    return A

A = [1, -2, 3, -4, 5, -6, 7, -8]

rearrangedA = swap(A)
print("Перемещенный массив A:", rearrangedA)

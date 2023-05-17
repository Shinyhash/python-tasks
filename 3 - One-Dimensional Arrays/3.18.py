def swap_adjacent_elements(A):
    for i in range(len(A)):
        if i % 2 == 0 and i + 1 < len(A):
            A[i], A[i+1] = A[i+1], A[i]

    return A

A = [10, 20, 30, 40, 50, 60, 70, 80]
modified_A = swap_adjacent_elements(A)
print("Измененный массив A:", modified_A)

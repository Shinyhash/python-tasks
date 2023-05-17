def compress_array(A):
    compressed_array = []

    for i in range(len(A)):
        if A[i] != 0:
            compressed_array.append(A[i])

    return compressed_array

A = [1, 0, 2, 0, 3, 0, 4]
compressed_A = compress_array(A)
print("Сжатый массив A:", compressed_A)

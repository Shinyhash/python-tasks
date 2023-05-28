def compress(A):
    compressedArr = []

    for i in range(len(A)):
        if A[i] != 0:
            compressedArr.append(A[i])

    return compressedArr

A = [1, 0, 2, 0, 3, 0, 4]

compressedA = compress(A)
print("Сжатый массив A:", compressedA)

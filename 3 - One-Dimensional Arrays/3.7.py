def evenElenents(arr):
    evenE = []
    oddE = []

    for num in arr:
        if num % 2 == 0:
            evenE.append(num)
        else:
            oddE.append(num)

    print("Четные элементы:")
    for num in evenE:
        print(num)

    print("Нечетные элементы:")
    for num in oddE:
        print(num)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evenElenents(array)

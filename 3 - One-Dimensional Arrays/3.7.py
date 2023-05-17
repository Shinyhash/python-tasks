def print_even_odd_elements(arr):
    even_elements = []
    odd_elements = []

    for num in arr:
        if num % 2 == 0:
            even_elements.append(num)
        else:
            odd_elements.append(num)

    print("Четные элементы:")
    for num in even_elements:
        print(num)

    print("Нечетные элементы:")
    for num in odd_elements:
        print(num)

array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print_even_odd_elements(array)

with open('6.10.f.txt', 'r') as file:
    n = file.readlines()

n = [float(num.strip()) for num in n]

ni = next((i for i, num in enumerate(n) if num < 0), None)

if ni is not None:
    
    sn = sum(n[:ni])
    print("Сумма чисел до первого отрицательного числа:", sn)
else:
    print("Отрицательное число не найдено в файле.")

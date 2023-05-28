def extract(number, N):
    fractionalP = str(number).split('.')[1]
    fractionalD = fractionalP[:N]
    return fractionalD

S = input("Введите вещественное число: ")
N = int(input("Введите целое число N: "))

number = float(S)
result = extract(number, N)
print("Набор символов, изображающих первые N цифр дробной части:", result)

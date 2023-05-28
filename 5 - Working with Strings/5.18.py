def extract(a):
    digitS = str(a)
    reversedD = list(reversed(digitS))
    return reversedD

a = int(input("Введите целое число: "))
digitsR = extract(a)
print("Набор символов, содержащий цифры числа в обратном порядке:", digitsR)

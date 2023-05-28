def extractD(a):
    digitS = str(a)
    return list(digitS)

a = int(input("Введите целое число: "))
b = extractD(a)
print("Набор символов, содержащий цифры числа:", b)

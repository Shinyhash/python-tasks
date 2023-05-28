def countD(inputS):
    digitC = 0
    for char in inputS:
        if char.isdigit():
            digitC += 1
    return digitC

inputT = input("Введите строку: ")
digitC = countD(inputT)
print("Количество цифр в строке:", digitC)

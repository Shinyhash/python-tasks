def countUL(inputS):
    uppercaseC = 0
    for char in inputS:
        if char.isupper():
            uppercaseC += 1
    return uppercaseC

inputT = input("Введите строку: ")
uppercaseC = countUL(inputT)
print("Количество прописных букв в строке:", uppercaseC)

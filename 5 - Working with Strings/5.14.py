def countLL(inputS):
    lowercaseC = 0
    for char in inputS:
        if char.islower():
            lowercaseC += 1
    return lowercaseC

inputT = input("Введите строку: ")
lowercaseC = countLL(inputT)
print("Количество строчных букв в строке:", lowercaseC)

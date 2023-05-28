def generate(c1, c2, length):
    alternateS = ""
    for i in range(length // 2):
        alternateS += c1 + c2
    return alternateS

c1 = input("Введите символ C1: ")
c2 = input("Введите символ C2: ")

length = int(input("Введите длину строки (четное число): "))

if length % 2 != 0:
    print("Длина строки должна быть четным числом.")
else:
    alternatingS = generate(c1, c2, length)
    print("Сгенерированная строка:", alternatingS)

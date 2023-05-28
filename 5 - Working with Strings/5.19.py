def combine(S1, S2, N1, N2):
    combinedS = S1[:N1] + S2[-N2:]
    return combinedS

N1 = int(input("Введите число N1: "))
N2 = int(input("Введите число N2: "))
S1 = input("Введите строку S1: ")
S2 = input("Введите строку S2: ")

result = combine(S1, S2, N1, N2)
print("Результат объединения строк:", result)

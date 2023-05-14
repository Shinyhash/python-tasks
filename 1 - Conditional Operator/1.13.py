C = input("Исходное направление: ")
N = int(input("Посланная команда (0 - продолжать движение, 1 - поворот налево, -1 - поворот направо): "))

if C == "С":
    if N == 0:
        print("Север")
    elif N == 1:
        print("Восток")
    elif N == -1:
        print("Запад")
elif C == "З":
    if N == 0:
        print("Запад")
    elif N == 1:
        print("Север")
    elif N == -1:
        print("Юг")
elif C == "Ю":
    if N == 0:
        print("Юг")
    elif N == 1:
        print("Запад")
    elif N == -1:
        print("Восток")
elif C == "В":
    if N == 0:
        print("Восток")
    elif N == 1:
        print("Юг")
    elif N == -1:
        print("Север")

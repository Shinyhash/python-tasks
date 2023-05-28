def determine(inputS):
    try:
        intV = int(inputS)
        return 1
    except ValueError:
        try:
            floatV = float(inputS)
            return 2
        except ValueError:
            return 0

inputS = input("Введите строку: ")
result = determine(inputS)

if result == 1:
    print("Строка представляет собой целое число.")
elif result == 2:
    print("Строка представляет собой вещественное число.")
else:
    print("Строку нельзя преобразовать в число.")

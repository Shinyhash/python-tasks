def validateIn(inputS):
    try:
        number = float(inputS)
        return True
    except ValueError:
        return False

inputN = input("Введите число: ")
isvalid = validateIn(inputN)

if isvalid:
    print("Ввод числа корректен")
else:
    print("Ввод содержит некорректные символы")

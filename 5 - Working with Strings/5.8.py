def convert(number):
    numberS = str(number)
    numberS = numberS.strip()
    numberS = numberS.replace(' ', '0')
    return numberS

inputN = float(input("Введите вещественное число: "))
convertedS = convert(inputN)
print("Преобразованная строка:", convertedS)

def parity(cityn):
    length = len(cityn)
    if length % 2 == 0:
        return True
    else:
        return False

city = input("Введите название города: ")

evenL = parity(city)
if evenL:
    print(f"Количество символов в городе {city} - четное")
else:
    print(f"Количество символов в городе {city} - нечетное")

a = int(input("Введите трехзначное число: "))

hundreds = a // 100
tens = (a // 10) % 10
ones = a % 10

if hundreds == ones:
    print("Палиндром")
else:
    print("Не палиндром")

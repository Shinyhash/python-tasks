a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a > b and a > c:
    if b > c:
        result = a * b
    else:
        result = a * c
elif b > a and b > c:
    if a > c:
        result = b * a
    else:
        result = b * c
else:
    if a > b:
        result = c * a
    else:
        result = c * b

print("Произведение двух наибольших чисел:", result)
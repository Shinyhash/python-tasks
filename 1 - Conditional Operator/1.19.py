d = int(input("Введите день: "))
m = int(input("Введите месяц: "))

if m == 2:
    daysM = 28
elif m in [4, 6, 9, 11]:
    daysM = 30
else:
    daysM = 31

if d < daysM:
    d += 1
else:
    d = 1
    m += 1
    if m == 13:
        m = 1

print("Следующая дата: ", d, ".", m)

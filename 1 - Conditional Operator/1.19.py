d = int(input("Введите день: "))
m = int(input("Введите месяц: "))

# Проверяем, сколько дней в месяце
if m == 2:
    days_in_month = 28
elif m in [4, 6, 9, 11]:
    days_in_month = 30
else:
    days_in_month = 31

# Проверяем, можно ли увеличить день на 1
if d < days_in_month:
    d += 1
else:
    d = 1
    m += 1
    if m == 13:
        m = 1

# Выводим результат
print("Следующая дата: ", d, ".", m)

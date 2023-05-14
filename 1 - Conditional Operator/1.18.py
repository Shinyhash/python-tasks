D = int(input("Введите день: "))
M = int(input("Введите месяц: "))

# определяем количество дней в месяце
if M == 2:
    days_in_month = 28
elif M in [4, 6, 9, 11]:
    days_in_month = 30
else:
    days_in_month = 31

# вычитаем из дня 1
D -= 1

# проверяем, не стал ли день равным 0
if D == 0:
    M -= 1
    if M == 0:
        M = 12
    days_in_month = 31 if M == 2 else 30 if M in [4, 6, 9, 11] else 31
    D = days_in_month

print("Предыдущая дата: {}.{}".format(D, M))

year = int(input("Введите год: "))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print(year, "год - високосный")
else:
    print(year, "год - не високосный")
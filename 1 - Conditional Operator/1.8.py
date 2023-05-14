x = float(input("x: "))
y = float(input("y: "))

if x > 0 and y > 0:
    print("Первая четверть")
elif x < 0 and y > 0:
    print("Вторая четверть")
elif x < 0 and y < 0:
    print("Третья четверть")
elif x > 0 and y < 0:
    print("Четвертая четверть")
else:
    print("Точка лежит на координатных осях")

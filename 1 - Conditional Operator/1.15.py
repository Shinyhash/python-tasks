import math

number = int(input("Введите номер элемента (1 - радиус, 2 - диаметр, 3 - длина, 4 - площадь круга): "))
value = float(input("Введите значение элемента: "))

if number == 1:
    diameter = value * 2
    length = 2 * math.pi * value
    area = math.pi * value ** 2
    print(f"Диаметр: {diameter}, Длина: {length}, Площадь: {area}")
elif number == 2:
    radius = value / 2
    length = 2 * math.pi * radius
    area = math.pi * radius ** 2
    print(f"Радиус: {radius}, Длина: {length}, Площадь: {area}")
elif number == 3:
    radius = value / (2 * math.pi)
    diameter = 2 * radius
    area = math.pi * radius ** 2
    print(f"Радиус: {radius}, Диаметр: {diameter}, Площадь: {area}")
elif number == 4:
    radius = math.sqrt(value / math.pi)
    diameter = 2 * radius
    length = 2 * math.pi * radius
    print(f"Радиус: {radius}, Диаметр: {diameter}, Длина: {length}")
else:
    print("Некорректный номер элемента")

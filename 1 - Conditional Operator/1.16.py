import math

# Вводим номер известного элемента и его значение
n = int(input("Введите номер известного элемента (1-4): "))
v = float(input("Введите значение известного элемента: "))

# Инициализируем переменные для остальных элементов
a = None
c = None
h = None
S = None

# Вычисляем остальные элементы в зависимости от известного элемента
if n == 1:
    a = v
    c = v * math.sqrt(2)
    h = v / math.sqrt(2)
    S = v**2 / 2
elif n == 2:
    c = v
    a = v / math.sqrt(2)
    h = v / math.sqrt(2)
    S = v**2 / 2
elif n == 3:
    h = v
    c = v * math.sqrt(2)
    a = v * math.sqrt(2)
    S = v**2 / 2
elif n == 4:
    S = v
    a = math.sqrt(2 * v)
    c = a * math.sqrt(2)
    h = a / math.sqrt(2)

# Выводим результаты вычислений
print("Катет a:", a)
print("Гипотенуза c:", c)
print("Высота h:", h)
print("Площадь S:", S)

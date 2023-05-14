a = float(input("Введите длину кирпича: "))
b = float(input("Введите ширину кирпича: "))
c = float(input("Введите высоту кирпича: "))
x = float(input("Введите ширину отверстия: "))
y = float(input("Введите высоту отверстия: "))

if (a <= x and b <= y) or (a <= y and b <= x) or \
   (a <= x and c <= y) or (a <= y and c <= x) or \
   (b <= x and c <= y) or (b <= y and c <= x):
  print("Кирпич поместится в отверстие")
else:
  print("Кирпич не поместится в отверстие")

def find(string):
    words = string.split()
    shortestw = min(words, key=len)
    shortestwl = len(shortestw)
    return shortestw, shortestwl

inputs = "Первый Четвертый Восьмидесятый Два"
shortestw, shortestwl = find(inputs)

print("Исходная строка:", inputs)
print("Самое короткое слово:", shortestw)
print("Длина самого короткого слова:", shortestwl)

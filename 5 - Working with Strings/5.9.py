def countFL(text):
    frequencyV = [0] * 26
    for char in text:
        if char.islower():
            index = ord(char) - ord('a')
            frequencyV[index] += 1
    return frequencyV

inputT = input("Введите строку: ")
frequency = countFL(inputT)

print("Частота встречаемости строчных латинских букв:")
for i, count in enumerate(frequency):
    letter = chr(ord('a') + i)
    print(f"{letter}: {count}")

def countw(string):
    w = string.split()
    return len(w)

inputs = "раз два три, слон жираф"
count = countw(inputs)
print("Количество слов в строке:", count)

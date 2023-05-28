def unnecessarySpaces(string):
    cleaneds = ' '.join(string.split())
    return cleaneds

inputs = "раз            два                 три"
cleaneds = unnecessarySpaces(inputs)
print("Исходная строка:", inputs)
print("Очищенная строка:", cleaneds)

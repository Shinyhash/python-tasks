def replaceW(text, oldW, newW):
    words = text.split()
    replacedWS = []
    for word in words:
        if word == oldW:
            replacedWS.append(newW)
        else:
            replacedWS.append(word)
    replacedT = ' '.join(replacedWS)
    return replacedT

inputS = "Это пример текста, где нужно заменить слова с такой же длиной"
oldW = "слова"
newW = "термин"
replacedT = replaceW(inputS, oldW, newW)

print("Исходный текст:", inputS)
print("Текст после замены:", replacedT)

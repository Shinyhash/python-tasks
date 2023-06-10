def abc(fp):
    with open(fp, 'r') as file:
        ln = file.readlines()

    l = max(ln, key=len)
    return l

fp = '6.21.f.txt'

l = abc(fp)
print("Самая длинная строка:")
print(l)

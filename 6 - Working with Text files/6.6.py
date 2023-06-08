with open('6.6.f.txt', 'r', encoding='utf-8') as file:
    c = file.read()

l = []
r = []

for char in c:
    if char.isalpha():
        if char.isascii():
            l.append(char)
        else:
            r.append(char)

with open('6.6.h.txt', 'w', encoding='utf-8') as file:
    file.write(''.join(l))

with open('6.6.g.txt', 'w', encoding='utf-8') as file:
    file.write(''.join(r))

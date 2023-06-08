with open('6.1.f.txt', 'r') as file:
    n = file.readlines()

a = []
b = []

for n in n:
    n = int(n.strip())
    if n % 2 == 0:
        a.append(str(n))
    else:
        b.append(str(n))

with open('6.1.g.txt', 'w') as file:
    file.write('\n'.join(a))

with open('6.1.h.txt', 'w') as file:
    file.write('\n'.join(b))

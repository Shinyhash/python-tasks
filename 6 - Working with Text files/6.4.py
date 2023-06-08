with open('6.4.f.txt', 'r') as file:
    n = file.readlines()

pn = []
nn = []

for n2 in n:
    n2 = int(n2.strip())
    if n2 > 0:
        pn.append(str(n2))
    elif n2 < 0:
        nn.append(str(n2))

with open('6.4.g.txt', 'w') as file:
    file.write('\n'.join(pn))

with open('6.4.h.txt', 'w') as file:
    file.write('\n'.join(nn))

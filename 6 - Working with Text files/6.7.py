with open('6.7.f.txt', 'r') as file:
    c = file.read()

c = c.replace('a', '')

with open('6.7.out.txt', 'w') as file:
    file.write(c)

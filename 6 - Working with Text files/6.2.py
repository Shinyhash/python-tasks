with open('6.2.in.txt', 'r') as file:
    a = file.read()

a = a.replace(' ', '')

with open('6.2.out.txt', 'w') as file:
    file.write(a)
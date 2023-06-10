def abc(fp):
    with open(fp, 'r') as file:
        pl = file.readlines()

    s = []

    for line in pl:
        for char in line:
            if char == '(':
                s.append('(')
            elif char == ')':
                if len(s) == 0 or s.pop() != '(':
                    return False

    return len(s) == 0

fp = '6.19.f.txt'

if abc(fp):
    print("Скобки в программе сбалансированы")
else:
    print("Скобки в программе несбалансированы")

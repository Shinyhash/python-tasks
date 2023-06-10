def abc(inp, out):
    with open(inp, 'r') as file:
        n = file.read().split()
        pn = [num for num in n if int(num) > 0]

    with open(out, 'w') as file:
        file.write(' '.join(pn))

inp = '6.16.f.txt'
out = '6.16.f2.txt'

abc(inp, out)

def abc(inp, out):
    with open(inp, 'r') as file:
        l = file.readlines()

    with open(out, 'w') as file:
        for i, line in enumerate(l, 1):
            fl = f"{i:4d} {line}"
            file.write(fl)

inp = '6.17.f.txt'
out = '6.17.f2.txt'

abc(inp, out)

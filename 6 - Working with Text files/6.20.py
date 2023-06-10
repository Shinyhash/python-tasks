def abc(inp, out):
    with open(inp, 'r') as file_f:
        c = file_f.read()

    i = c.replace('0', 'x').replace('1', '0').replace('x', '1')

    with open(out, 'w') as file_g:
        file_g.write(i)

inp = '6.20.f.txt'
out = '6.20.g.txt'

abc(inp, out)

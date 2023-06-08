def abc(fp, fo):
    ml = []
    
    for f in fp:
        with open(f, 'r') as file:
            ml.extend(file.readlines())
    
    ml.sort()
    
    with open(fo, 'w') as file:
        for line in ml:
            line = line.rstrip('\n')
            pk = line.ljust(80)
            file.write(pk + '\n')

fp = ['6.14.f.txt', '6.14.f2.txt']
fo = '6.14.f3.txt'

abc(fp, fo)

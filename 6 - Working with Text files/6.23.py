def abc(fp, ss):
    ml = []

    with open(fp, 'r') as file:
        ls = file.readlines()

    for l in ls:
        if ss in l:
            ml.append(l)

    return ml

fp = '6.23.f.txt'
ss = 's'

ml = abc(fp, ss)
print("Строки из файла f, содержащие фрагмент строки s:")
for l in ml:
    print(l)

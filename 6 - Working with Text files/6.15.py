def fmn(fp):
    with open(fp, 'r') as file:
        n = file.read().split()
        mn = float(n[0])

        for n in n:
            cn = float(n)
            if cn > mn:
                mn = cn

    return mn

fp = '6.15.f.txt'

mn = fmn(fp)
print("Наибольшее число:", mn)

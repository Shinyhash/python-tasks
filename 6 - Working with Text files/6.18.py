def abc(fp):
    with open(fp, 'r') as file:
        l = file.readlines()

    sl = min(l, key=len)
    print("Первая из самых коротких строк:")
    print(sl)

fp = '6.18.f.txt'

abc(fp)

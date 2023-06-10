def abc(fpf, fpg):
    with open(fpf, 'r') as ff:
        lf = ff.readlines()

    sl = [line.rstrip() for line in lf]

    with open(fpg, 'w') as fg:
        fg.write('\n'.join(sl))

fpf = '6.24.f.txt'
fpg = '6.24.g.txt'

abc(fpf, fpg)
print("Пробелы в концах строк файла f1 исключены. Результат записан в файл f2.")

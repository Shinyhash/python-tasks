def abc(fp):
    with open(fp, 'r') as file:
        c = file.read()

    w = c.split()
    return len(w)

def abcd(fpf, fpg):
    with open(fpf, 'r') as ff:
        cf = ff.read()

    w = cf.split()

    with open(fpg, 'w') as fg:
        for word in w:
            fg.write(word + '\n')

fpf = '6.22.f.txt'
fpg = '6.22.g.txt'

wc = abc(fpf)
print("Количество слов в файле f:", wc)

abcd(fpf, fpg)
print("Слова из файла f записаны в файл g.")

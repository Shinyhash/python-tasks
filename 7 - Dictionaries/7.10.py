def abc(l):
    print("Расписание учителя:")
    for ln, li in l.items():
        print(f"Номер урока: {ln}")
        print(f"Время начала: {li['t']}")
        print(f"Класс: {li['c']}")
        print(f"Предмет: {li['p']}")
        print(f"Номер кабинета: {li['r']}")
        print()

s = {
    1: {
        't': '8:00',
        'c': '7А',
        'p': 'Математика',
        'r': 321
    },
    2: {
        't': '9:00',
        'c': '7Б',
        'p': 'Русский язык',
        'r': 123
    },
    3: {
        't': '10:00',
        'c': '7C',
        'p': 'История',
        'r': 231
    },
}

abc(s)
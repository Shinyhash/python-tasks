def abc(sd):
    print("Сведения о студентах:")
    for s, d in sd.items():
        print(f"Ф.И.О.: {s}")
        print(f"Курс: {d['c']}")
        print(f"Группа: {d['g']}")
        print(f"Номер зачетки: {d['z']}")
        print(f"Средний балл: {d['a']}")
        print()

sf = {
    'Иванов Иван Иванович': {
        'c': 2,
        'g': '2По-123',
        'z': '543531',
        'a': 4.8
    },
    'Петров Петр Петрович': {
        'c': 3,
        'g': '3Веб-234',
        'z': '654353',
        'a': 4.5
    }
}

abc(sf)

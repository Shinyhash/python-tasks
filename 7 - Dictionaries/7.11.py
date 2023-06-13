def abc(s):
    print("Расписание полетов самолетов:")
    for f, d in s.items():
        print(f"Пункт посадки: {d['dp']}")
        print(f"Время отправления: {d['dt']}")
        print(f"Время прибытия: {d['a']}")
        print(f"Время полета: {d['ft']}")
        print(f"Стоимость билета: {d['pr']} Тг.")
        print()

t = {
    'Краков': {
        'dp': 'Москва',
        'dt': '12:00',
        'a': '16:30',
        'ft': '4 часа',
        'pr': 8000
    },
    'Рим': {
        'dp': 'Москва',
        'dt': '14:30',
        'a': '18:00',
        'ft': '3 часа',
        'pr': 5500
    },
    'Токио': {
        'dp': 'Москва',
        'dt': '20:30',
        'a': '08:00',
        'ft': '5 часов',
        'pr': 7000
    }
}

abc(t)
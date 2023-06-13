def abc(s):
    print("Анкетные данные учеников:")
    for ss, d in s.items():
        print(f"Ф.И.О.: {ss}")
        print(f"Год рождения: {d['yr']}")
        print(f"Адрес: {d['ad']}")
        
        print("Сведения о родителях:")
        print(f"Имя отца: {d['pr']['f']}")
        print(f"Имя матери: {d['pr']['m']}")
        print()

s = {
    'Иванов Иван Иванович': {
        'yr': 1998,
        'ad': 'г. Москва, ул. Пушкина, д. 10',
        'pr': {
            'f': 'Иванов Иван Иванович',
            'm': 'Иванова Мария Петровна'
        }
    }
}

abc(s)

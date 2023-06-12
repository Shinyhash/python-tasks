def abc(s):
    print("Анкетные данные учеников:")
    for st, details in s.items():
        print(f"Ф.И.О.: {st}")
        print(f"Год рождения: {details['yr']}")
        print(f"Адрес: {details['ad']}")
        
        print("Сведения о родителях:")
        print(f"Имя отца: {details['pr']['f']}")
        print(f"Имя матери: {details['pr']['m']}")
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

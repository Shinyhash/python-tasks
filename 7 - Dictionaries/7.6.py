def abc(book):
    print("Список книг:")
    for b, d in book.items():
        print(f"Автор: {d['au']}")
        print(f"Название: {b}")
        print(f"Издательство: {d['pb']}")
        print(f"Год: {d['yr']}")
        print(f"Стоимость: {d['pr']} тг.")
        print()

l = {
    '1984': {
        'au': 'Джордж Оруэлл',
        'pb': 'Эксмо',
        'yr': 2015,
        'pr': 500
    },
    'Преступление и наказание': {
        'au': 'Федор Достоевский',
        'pb': 'ACT',
        'yr': 2012,
        'pr': 500
    },
    'Гарри Поттер и философский камень': {
        'au': 'Дж. К. Роулинг',
        'pb': 'Росмэн',
        'yr': 1999,
        'pr': 500
    }
}

abc(l)
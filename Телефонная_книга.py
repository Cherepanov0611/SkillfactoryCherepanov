contacts = {} 
for i in range(3):

    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    contacts[name] = phone

# вывести только имена из телефонной книги
print(contacts.keys())

# вывести только телефоны из телефонной книги
print(contacts.values())

print()
for name, phone in contacts.items():
    print(f'Контакт: {name} Телефон: {phone}')

# добавить две новые записи в словарь
print('Добавляем новые записи в словарь:')
for i in range(2):
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    contacts[name] = phone
    print('Запись добавлена в словарь')

# редактируем запись в словаре:
print('Редактируем запись в словарь:')
print(contacts)
name = input('Введите имя из словаря: ')
phone = input('Введите новый номер телефона: ')
contacts[name] = phone
print('Запись отредактирована')

# проверка на наличие записи в словаре:
print('Проверяем наличие записи в словарь:')
name = input('Введите имя: ')
if name in contacts.keys():
    del contacts[name]
    print('Запись удалена')
else:
    phone = input('Введите номер телефона: ')
    contacts[name] = phone
    print('Запись добавлена в словарь')

# выводим итоговый словарь:
print(contacts)

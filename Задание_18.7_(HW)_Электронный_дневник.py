import random

# Инициализация списка учеников и предметов
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
students.sort()  # Сортируем список учеников
classes = ['Математика', 'Русский язык', 'Информатика']
students_marks = {}  # Словарь для хранения оценок учеников

# Заполнение оценок для каждого ученика по предметам
for student in students:
    students_marks[student] = {}  # Инициализация словаря для ученика
    for class_ in classes:
        marks = [random.randint(1, 5) for i in range(3)]  # Генерация случайных оценок
        students_marks[student][class_] = marks  # Запись оценок в словарь

# Вывод списка учеников и их оценок
for student in students:
    print(f'{student}\n{students_marks[student]}')

# Инструкция по использованию программы
print('''
Список команд:
1. Добавить оценки ученика по предмету
2. Вывести средний балл по всем предметам по каждому ученику
3. Вывести все оценки по всем ученикам
4. Вывести оценки конкретного ученика
5. Вывести средний балл по конкретному предмету ученика
6. Изменить оценку ученика
7. Удалить оценку ученика
8. Удалить ученика
9. Поиск ученика по имени
10. Вывод списка всех учеников
11. Вывод количества оценок у ученика по всем предметам
12. Выход из программы
''')

# Основной цикл программы
while True:
    command = int(input('Введите команду: '))  # Считывание команды от пользователя

    if command == 1:
        # Добавление оценки ученика
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        mark = int(input('Введите оценку: '))
        if student in students_marks and class_ in students_marks[student]:
            students_marks[student][class_].append(mark)  # Добавление новой оценки
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')

    elif command == 2:
        # Вывод среднего балла по всем предметам для каждого ученика
        for student in students:
            if student in students_marks:  # Проверяем, существует ли ученик
                print(student)
                for class_ in classes:
                    if class_ in students_marks[student]:  # Проверяем, существует ли предмет
                        marks_sum = sum(students_marks[student][class_])  # Сумма оценок
                        marks_count = len(students_marks[student][class_])  # Количество оценок
                        average = marks_sum // marks_count if marks_count > 0 else 0  # Средний балл
                        print(f'{class_} - {average}')  # Вывод среднего балла
                print()

    elif command == 3:
        # Вывод всех оценок по всем ученикам
        for student in students:
            if student in students_marks:  # Проверяем, существует ли ученик
                print(student)
                for class_ in classes:
                    if class_ in students_marks[student]:  # Проверяем, существует ли предмет
                        print(f'\t{class_} - {students_marks[student][class_]}')  # Вывод оценок
                print()

    elif command == 4:
        # Вывод оценок конкретного ученика
        student = input('Введите имя ученика для вывода оценок: ')
        if student in students_marks:
            print(f'Оценки для {student}:')
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')  # Вывод оценок
        else:
            print('Ученик не найден')

    elif command == 5:
        # Вывод среднего балла по конкретному предмету для ученика
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        if student in students_marks and class_ in students_marks[student]:
            marks_sum = sum(students_marks[student][class_])  # Сумма оценок
            marks_count = len(students_marks[student][class_])  # Количество оценок
            average = marks_sum / marks_count if marks_count > 0 else 0  # Средний балл
            print(f'Средний балл для {student} по предмету {class_} - {average}')
        else:
            print('Ученик или предмет не найдены')

    elif command == 6:
        # Изменение оценки ученика
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        index = int(input('Введите номер оценки для изменения (1, 2, 3 и т. д.): ')) - 1
        if student in students_marks and class_ in students_marks[student] and 0 <= index < len(students_marks[student][class_]):
            new_mark = int(input('Введите новую оценку: '))
            students_marks[student][class_][index] = new_mark  # Изменение оценки
            print(f'Оценка изменена на {new_mark}')
        else:
            print('ОШИБКА: неверные данные')

    elif command == 7:
        # Удаление оценки ученика
        student = input('Введите имя ученика: ')
        class_ = input('Введите предмет: ')
        index = int(input('Введите номер оценки для удаления (1, 2, 3 и т. д.): ')) - 1
        if student in students_marks and class_ in students_marks[student] and 0 <= index < len(students_marks[student][class_]):
            removed_mark = students_marks[student][class_].pop(index)  # Удаление оценки
            print(f'Оценка {removed_mark} удалена у {student}')
        else:
            print('ОШИБКА: неверные данные')

    elif command == 8:
        # Удаление ученика
        student = input('Введите имя ученика для удаления: ')
        if student in students_marks:
            del students_marks[student]  # Удаление оценок ученика
            students.remove(student)  # Удаление ученика из списка
            print(f'{student} удален из списка учеников')
        else:
            print('Ученик не найден')

    # Команда для поиска ученика по имени
    elif command == 9:
            student_name = input('Введите имя ученика для поиска: ')
            if student_name in students_marks:
                print(f'Ученик {student_name} найден.')
            else:
                print('Ученик не найден.')

    # Команда для вывода списка всех учеников
    elif command == 10:
        print('Список всех учеников:')
        for student in students:
            print(student)
        print()

    # Команда для вывода количества оценок у ученика по всем предметам
    elif command == 11:
        student = input('Введите имя ученика для вывода количества оценок: ')
        if student in students_marks:
            total_marks = sum(
                len(students_marks[student][class_]) for class_ in classes if class_ in students_marks[student])
            print(f'У ученика {student} всего оценок: {total_marks}')
        else:
            print('Ученик не найден.')

    elif command == 12:
        print('Выход из программы')  # Завершение программы
        break

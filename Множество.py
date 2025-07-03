numbers = set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

            num = int(input('Введите число: '))
            if num in numbers:
                print('Удаляем число из множества')
                numbers.remove(num)
            else:
                print('Добавляем число в множество')
                numbers.add(num)
            
            print(f'Длина множества: {len(numbers)}')
            print(numbers)

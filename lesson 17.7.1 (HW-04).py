multipl = 1
for i in range(1, 11):
    if i % 2 == 0:  # проверка четности
        continue  # пропускаем четные числа
    multipl *= i  # умножаем нечетные числа
print(multipl)  # выводим итоговое произведение

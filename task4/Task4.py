# 1.
# Находишь среднее значение всех элементов массива.
# [1, 10, 2, 9]
# (1 + 10 + 2 + 9) / 4 = 5.5
#
# 2.
# Каждый элемент вычитаешь из среднего по модулю.
# - | 5.5 - 1 | = 4.5
# - | 5.5 - 10 | = 4.5
# - | 5.5 - 2 | = 3.5
# - | 5.5 - 9 | = 3.5
#
# 3.
# Берёшь за базу значение с наименьшей разницей.
# Вариант 1 - 2
# Вариант 2 - 9
#
# 4.
# Смотришь сколько на каждый элемент надо прибавить по + 1 до достижения выбранного значения.
# Вариант 1:
# 1 - +1
# 10 - +8
# 2 - 0
# 9 - +7
# Вариант 2:
# 1 - +8
# 10 - +1
# 2 - +7
# 9 - 0
#
# 5.
# Складываешь сколько раз увеличил - получаешь результат.
# Вариант 1:
# 1 + 8 + 7 = 16
# Вариант 2:
# 8 + 1 + 7 = 16


import sys
import os

if len(sys.argv) != 2:
    print("Использование: python Task4.py <путь_к_файлу>")
    sys.exit(1)

file_path = sys.argv[1]

if not os.path.exists(file_path):
    print(f"Файл не найден: {file_path}")
    sys.exit(1)

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        numbers = [int(line.strip()) for line in f if line.strip().isdigit()]

    if not numbers:
        print("Файл не содержит чисел.")
        sys.exit(1)

    average = sum(numbers) / len(numbers)

    differences = [abs(number - average) for number in numbers]
    min_diff = min(differences)
    closest_number = numbers[differences.index(min_diff)]

    steps = sum(abs(number - closest_number) for number in numbers)

    print(f"Число с минимальной разницей от среднего: {closest_number}")
    print(f"Общее количество шагов для приведения всех чисел к этому числу: {steps}")

except Exception as error:
    print(f"Ошибка при обработке файла: {error}")
    sys.exit(1)
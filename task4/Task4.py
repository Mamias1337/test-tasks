import sys
import os

    #Проверка количества аргументов командной строки.
if len(sys.argv) != 2:
    print("Использование: python Task4.py <путь_к_файлу>")
    sys.exit(1)

    #Проверка существования указанного файла.
file = sys.argv[1]

if not os.path.exists(file):
    print(f"Файл не найден: {file}")
    sys.exit(1)

    #Чтение чисел из файла.
try:
    with open(file_path, 'r', encoding='utf-8') as f:
        numbers = [int(line.strip()) for line in f if line.strip().isdigit()]

    #Проверка наличия чисел в файле.
    if not numbers:
        print("Файл не содержит чисел.")
        sys.exit(1)

    average = sum(numbers) / len(numbers)

    #Поиск числа, наиболее близкого к среднему.
    differences = [abs(number - average) for number in numbers]
    min_diff = min(differences)
    closest_number = numbers[differences.index(min_diff)]

    steps = sum(abs(number - closest_number) for number in numbers)

    print(f"Число с минимальной разницей от среднего: {closest_number}")
    print(f"Общее количество шагов для приведения всех чисел к этому числу: {steps}")

except Exception as error:
    print(f"Ошибка при обработке файла: {error}")
    sys.exit(1)
import json
import sys
import os


    # Проверка на количество аргументов.
if len(sys.argv) !=4:
    print('Использование: python task3.py <tests.json> <values.json> <report.json>')
    sys.exit(1)

    # Проверка наличия файлов.
if not os.path.isfile(sys.argv[1]):
    print('Файл tests.json не существует.')
    sys.exit(1)

if not os.path.isfile(sys.argv[2]):
    print('Файл values.json не существует.')
    sys.exit(1)

    # Загрузка данных из файлов
with open(sys.argv[1], "r") as f:  # tests.json
    tests_data = json.load(f)

with open(sys.argv[2], "r") as f:  # values.json
    values_data = json.load(f)

    # Преобразуем values в словарь для быстрого доступа
values_list = {item["id"]: item["value"] for item in values_data["values"]}


    # Рекурсивная функция для вставки значений
def fill_values(tests):
    for test in tests:
        test_id = test.get("id")
        if test_id in values_list:
            test["value"] = values_list[test_id]
        if "values" in test:
            fill_values(test["values"])

    # Обработка тестов
fill_values(tests_data["tests"])

    # Сохранение результата в report.json
with open(sys.argv[4], "w") as f:
    json.dump(tests_data, f, indent=4)

    print('report.json успешно изменён.')
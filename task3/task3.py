import json
import sys
import os

    # Проверка на количество аргументов.
if len(sys.argv) != 4:
    print('Использование: python task3.py <values.json> <tests.json> <report.json>')
    sys.exit(1)

    # Проверка наличия файлов.

if not os.path.isfile(sys.argv[1]):
    print('Файл values.json не существует.')
    sys.exit(1)


if not os.path.isfile(sys.argv[2]):
    print('Файл tests.json не существует.')
    sys.exit(1)


    # Загрузка данных из файлов
with open(sys.argv[1], "r", encoding="utf-8") as f:
    values_data = json.load(f)


with open(sys.argv[2], "r", encoding="utf-8") as f:
    tests_data = json.load(f)



    # Преобразуем values в словарь для быстрого доступа
values_list = {}
for item in values_data["values"]:
    values_list[item["id"]] = item["value"]


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
with open(sys.argv[3], "w", encoding="utf-8") as f:
    json.dump(tests_data, f, indent=4)

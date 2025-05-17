import json
import sys

if len(sys.argv) !=4:
    print('Использование: python task3.py <tests.json> <values.json> <report.json>')
    sys.exit(1)

# Загрузка данных из файлов
with open(sys.argv[3], "r") as f:
    values_data = json.load(f)

with open(sys.argv[2], "r") as f:
    tests_data = json.load(f)

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
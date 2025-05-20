import sys

def circular_mass(n, m):
    arr = list(range(1, n + 1))  # Создаём список чисел от 1 до n включительно.
    path = []   # Список, в который будем добавлять элементы в порядке обхода.
    index = 0   # Начальный индекс.

    for _ in range(n):      # Повторяем n раз, пока не обойдем все элементы.
        path.append(arr[index])     # Добавляем текущий элемент в результат (путь).
        index = (index + m - 1) % n # Сдвигаемся по кругу на m-1 шагов.
        if index < 0:  # Обрабатываем отрицательный индекс
            index += n

    return path

if __name__ == "__main__":
    # Проверка количества аргументов командной строки.
    if len(sys.argv) != 3:
        print("Использование: python circular_mass.py <n> <m>")
        sys.exit(1)

    # Преобразуем аргументы командной строки в целые числа.
    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("Параметры n и m должны быть целыми числами.")
        sys.exit(1)

    # Вызов функции circular_mass и вывод результата.
    result = circular_mass(n, m)
    print(''.join(map(str, result)))
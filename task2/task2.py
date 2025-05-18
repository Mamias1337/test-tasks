import sys
import math
import os

    # Проверка количества аргументов командной строки.
if len(sys.argv) !=3:
    print('Использование: python task2.py <center_and_rad.txt> <points.txt>')
    sys.exit(1)

    # Проверка существования указанных файлов.
if not os.path.isfile(sys.argv[2]):
    print('Файл points.txt не существует.')
    sys.exit(1)

if not os.path.isfile(sys.argv[1]):
    print('Файл center_and_rad.txt не существует.')
    sys.exit(1)

    # Чтение центра и радиуса из файла.
with open(sys.argv[1], 'r', encoding='utf-8') as f:
    if os.stat(sys.argv[1]).st_size == 0:
        print(f'Файл {sys.argv[1]} пустой.')
        sys.exit(1)
    else:
        center_line = f.readline().strip()
        radius_line = f.readline().strip()

        center = list(map(float, center_line.split()))
        radius = float(radius_line)

    # Чтение точек из второго файла.
with open(sys.argv[2], 'r', encoding='utf-8') as f:

    if os.stat(sys.argv[2]).st_size == 0:
        print(f'Файл {sys.argv[2]} пустой.')
        sys.exit(1)
    else:
        point_list = []

        for line in f:
            line = line.strip()
            if line:


                coord = list(map(float, line.split()))
                point_list.append(coord)

    # Проверка количества точек.
if not 1 <= len(point_list) <= 100:
    print(f'Количество точек вне диапазона 1-100, а именно: {len(point_list)}.')
    sys.exit(1)

    # Расчёт расстояния от точки до центра окружности и определение положения точки относительно окружности.
for point in point_list:
    d = math.sqrt(math.pow(point[0] - center[0], 2) + math.pow(point[1] - center[1], 2))
    if d < radius:
        print(f"1 - точка [{point[0]};{point[1]}] лежит внутри окружности c центром в точках {center} и радиусом {radius}.")
    if d > radius:
        print(f"2 - точка [{point[0]};{point[1]}] лежит вне окружности c центром в точках {center} и радиусом {radius}.")
    if d == radius:
        print(f"0 - точка [{point[0]};{point[1]}] лежит на окружности c центром в точках {center} и радиусом {radius}.")

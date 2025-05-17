import sys

def circular_mass(n, m):
    arr = list(range(1, n + 1))
    path = []
    index = 0

    for _ in range(n):
        path.append(arr[index])
        index = (index + m - 1) % n

    return path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Использование: python circular_mass.py <n> <m>")
        sys.exit(1)

    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("Параметры n и m должны быть целыми числами.")
        sys.exit(1)

    result = circular_mass(n, m)
    print("Путь:", ''.join(map(str, result)))
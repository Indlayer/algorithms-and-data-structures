def input_int(prompt, default_val):
    try:
        val = input(f"{prompt} [по умолчанию {default_val}]: ").strip()
        return int(val) if val else int(default_val)
    except (ValueError, EOFError):
        return int(default_val)

def input_list_int(prompt, default_str):
    try:
        val = input(f"{prompt} [по умолчанию {default_str}]: ").strip()
        s = val if val else default_str
        arr = [int(x) for x in s.split()]
        arr.sort()
        return arr
    except (ValueError, EOFError):
        arr = [int(x) for x in default_str.split()]
        arr.sort()
        return arr

# Итеративный бинарный поиск
def binary_search_iterative(arr: list, target, trace: bool = False):
    left = 0
    right = len(arr) - 1
    steps = 0

    if trace:
        print(f"Поиск числа {target} в массиве: {arr}")

    while left <= right:
        steps += 1
        mid = (left + right) // 2
        val = arr[mid]
        if trace:
            print(f"Шаг {steps}: диапазон [{left}..{right}], индекс mid={mid}, значение arr[{mid}]={val}")

        if val == target:
            if trace:
                print(f"  -> Найдено на индексе {mid} за {steps} шагов!")
            return mid, steps
        elif val < target:
            if trace:
                print(f"  -> {val} < {target}: отбрасываем левую часть, смещаем left в {mid + 1}")
            left = mid + 1
        else:
            if trace:
                print(f"  -> {val} > {target}: отбрасываем правую часть, смещаем right в {mid - 1}")
            right = mid - 1

    if trace:
        print(f"  -> Число не найдено после {steps} шагов.")
    return -1, steps

# Рекурсивный бинарный поиск
def binary_search_recursive(arr: list, target, left: int = 0, right: int = None, steps: int = 0):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1, steps
    steps += 1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid, steps
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right, steps)
    else:
        return binary_search_recursive(arr, target, left, mid - 1, steps)

# Поиск диапазона вхождений (для массивов с повторами)
def find_bounds(arr: list, target):
    l, r = 0, len(arr) - 1
    first = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            first = m
            r = m - 1
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1

    l, r = 0, len(arr) - 1
    last = -1
    while l <= r:
        m = (l + r) // 2
        if arr[m] == target:
            last = m
            l = m + 1
        elif arr[m] < target:
            l = m + 1
        else:
            r = m - 1

    return first, last

def run_all_demo():
    data = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]
    print("\n1. Пошаговая трассировка (успешный поиск числа 23):")
    idx, steps = binary_search_iterative(data, 23, trace=True)
    print(f"Результат: индекс = {idx}, шагов = {steps}\n")

    print("2. Пошаговая трассировка (число 50 отсутствует):")
    idx_no, steps_no = binary_search_iterative(data, 50, trace=True)
    print(f"Результат: индекс = {idx_no}, шагов = {steps_no}\n")

    print("3. Сравнение итеративной и рекурсивной реализации (ищем 91):")
    it_idx, it_s = binary_search_iterative(data, 91, trace=False)
    rec_idx, rec_s = binary_search_recursive(data, 91)
    print(f"  Итеративный: индекс {it_idx}, шагов {it_s}")
    print(f"  Рекурсивный: индекс {rec_idx}, шагов {rec_s}\n")

    data_dups = [1, 3, 5, 5, 5, 5, 7, 9, 11]
    f, l = find_bounds(data_dups, 5)
    print(f"4. Поиск диапазона числа 5 в {data_dups}:")
    print(f"  Первое вхождение: {f}, последнее: {l} (всего {l - f + 1} элементов)")

def run_interactive():
    print("\nВведите отсортированный массив чисел (если не отсортирован — программа автоматически отсортирует):")
    arr = input_list_int("Массив", "2 5 8 12 16 23 38 45 56 72 91")
    target = input_int("Введите искомое число", 23)
    idx, steps = binary_search_iterative(arr, target, trace=True)
    if idx != -1:
        print(f"\n-> Элемент {target} найден на позиции (индекс) {idx} за {steps} шагов.")
    else:
        print(f"\n-> Элемент {target} в массиве не найден (затрачено {steps} шагов).")

def main():
    print("=" * 60)
    print("Лабораторная работа №10: Бинарный поиск")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    print("\nВыберите режим работы:")
    print("1 - Запустить авто-демонстрацию всех проверок")
    print("2 - Ввести свой массив и число для пошагового поиска")
    try:
        mode = input("Ваш выбор (1 или 2) [по умолчанию 1]: ").strip()
    except (EOFError, KeyboardInterrupt):
        mode = "1"

    if mode == "2":
        run_interactive()
    else:
        run_all_demo()
    print("=" * 60)

if __name__ == "__main__":
    main()

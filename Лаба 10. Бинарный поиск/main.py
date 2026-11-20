def binary_search_iterative(arr: list, target, trace: bool = False):
    """
    Итеративная реализация бинарного поиска в отсортированном массиве.
    Возвращает (индекс элемента или -1, количество проверок).
    """
    left = 0
    right = len(arr) - 1
    steps = 0
    
    if trace:
        print(f"Поиск элемента {target} в массиве: {arr}")
        
    while left <= right:
        steps += 1
        mid = (left + right) // 2
        val = arr[mid]
        if trace:
            print(f"Шаг {steps}: диапазон [{left}..{right}], mid={mid}, значение arr[{mid}]={val}")
            
        if val == target:
            if trace:
                print(f"  -> Элемент найден на позиции {mid} за {steps} шагов.")
            return mid, steps
        elif val < target:
            if trace:
                print(f"  -> {val} < {target}: смещаем левую границу в {mid + 1}")
            left = mid + 1
        else:
            if trace:
                print(f"  -> {val} > {target}: смещаем правую границу в {mid - 1}")
            right = mid - 1
            
    if trace:
        print(f"  -> Элемент не найден после {steps} шагов.")
    return -1, steps

def binary_search_recursive(arr: list, target, left: int = 0, right: int = None, steps: int = 0):
    """Рекурсивная реализация бинарного поиска."""
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

def find_bounds(arr: list, target):
    """Поиск первого и последнего вхождения элемента (левый и правый бинпоиск)."""
    # Левая граница
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
            
    # Правая граница
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

def main():
    print("=" * 60)
    print("Лабораторная работа №10: Бинарный поиск")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    data = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]

    # 1. Трассировка успешного поиска
    print("1. Пошаговая трассировка (успешный поиск):")
    idx, steps = binary_search_iterative(data, 23, trace=True)
    print(f"Результат: индекс = {idx}, шагов = {steps}\n")

    # 2. Трассировка неуспешного поиска
    print("2. Пошаговая трассировка (элемент отсутствует):")
    idx_no, steps_no = binary_search_iterative(data, 50, trace=True)
    print(f"Результат: индекс = {idx_no}, шагов = {steps_no}\n")

    # 3. Сравнение итеративной и рекурсивной реализации
    print("3. Сравнение реализаций (ищем 91):")
    it_idx, it_s = binary_search_iterative(data, 91, trace=False)
    rec_idx, rec_s = binary_search_recursive(data, 91)
    print(f"  Итеративный: индекс {it_idx}, шагов {it_s}")
    print(f"  Рекурсивный: индекс {rec_idx}, шагов {rec_s}\n")

    # 4. Поиск в массиве с повторениями (левая и правая границы)
    data_with_dups = [1, 3, 5, 5, 5, 5, 7, 9, 11]
    f, l = find_bounds(data_with_dups, 5)
    print(f"4. Поиск диапазона вхождений числа 5 в {data_with_dups}:")
    print(f"  Первое вхождение: индекс {f}, последнее вхождение: индекс {l} (всего {l - f + 1} элементов)")

    print("=" * 60)

if __name__ == "__main__":
    main()

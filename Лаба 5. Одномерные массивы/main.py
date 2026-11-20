def task_1(n: int) -> list:
    """Задача 1: Массив из N первых положительных нечетных чисел: 1, 3, 5..."""
    return [2 * i + 1 for i in range(n)]

def task_2(n: int, a: float, d: float) -> list:
    """Задача 2: Массив первых N членов геометрической прогрессии: A, A*D, A*D^2..."""
    res = []
    curr = a
    for _ in range(n):
        res.append(curr)
        curr *= d
    return res

def task_3(n: int, a: int, b: int) -> list:
    """Задача 3: Массив размера N: A1=A, A2=B, каждый следующий = сумме всех предыдущих."""
    arr = [a, b]
    current_sum = a + b
    for _ in range(2, n):
        arr.append(current_sum)
        current_sum += current_sum  # удвоение суммы, так как добавили current_sum
    return arr

def task_4(arr: list) -> list:
    """Задача 4: Порядок вывода: A1, AN, A2, AN-1, A3, AN-2..."""
    res = []
    left = 0
    right = len(arr) - 1
    while left <= right:
        res.append(arr[left])
        if left != right:
            res.append(arr[right])
        left += 1
        right -= 1
    return res

def task_5(arr: list) -> list:
    """Задача 5: Вначале элементы с нечетными номерами (A1, A3...) по возрастанию номеров,
    затем с четными номерами (A2, A4...) по убыванию номеров (1-based нумерация)."""
    odd_positions = [arr[i] for i in range(0, len(arr), 2)]  # A1, A3, A5 (индексы 0, 2, 4)
    even_positions = [arr[i] for i in range(1, len(arr), 2)]  # A2, A4, A6 (индексы 1, 3, 5)
    even_positions.reverse()
    return odd_positions + even_positions

def task_6(arr: list, k: int, l: int) -> float:
    """Задача 6: Среднее арифметическое элементов с номерами от K до L включительно (1-based)."""
    # 1 <= K <= L <= N
    sub = arr[k - 1:l]
    return sum(sub) / len(sub)

def task_7(arr: list):
    """Задача 7: Проверить, образуют ли элементы арифметическую прогрессию.
    Если да — разность, если нет — 0."""
    if len(arr) < 2:
        return 0
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            return 0
    return diff

def task_8(arr: list):
    """Задача 8: Минимальный элемент из элементов с четными номерами: A2, A4, A6... (1-based)."""
    # Элементы с четными номерами — это индексы 1, 3, 5...
    even_numbered = [arr[i] for i in range(1, len(arr), 2)]
    if not even_numbered:
        return None
    return min(even_numbered)

def task_9(arr: list) -> int:
    """Задача 9: Номер (1-based) последнего локального максимума.
    Локальный максимум — элемент, больший любого из своих соседей."""
    n = len(arr)
    last_max_index = -1
    for i in range(n):
        left_ok = (i == 0) or (arr[i] > arr[i - 1])
        right_ok = (i == n - 1) or (arr[i] > arr[i + 1])
        if left_ok and right_ok:
            last_max_index = i + 1  # 1-based
    return last_max_index

def task_10(arr: list) -> tuple:
    """Задача 10: Найти номера (1-based) двух одинаковых элементов в порядке возрастания."""
    seen = {}
    for i, val in enumerate(arr, 1):
        if val in seen:
            return seen[val], i
        seen[val] = i
    return None

def main():
    print("=" * 60)
    print("Лабораторная работа №5: Одномерные массивы")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    # 1. Нечетные числа
    print(f"Задание 1: N=7 => {task_1(7)}")

    # 2. Геометрическая прогрессия
    print(f"Задание 2: N=5, A=2, D=3 => {task_2(5, 2, 3)}")

    # 3. Сумма предыдущих
    print(f"Задание 3: N=6, A=1, B=2 => {task_3(6, 1, 2)}")

    # 4. Вывод A1, AN, A2, AN-1...
    a4 = [10, 20, 30, 40, 50, 60]
    print(f"Задание 4: Исходный={a4} => {task_4(a4)}")

    # 5. Нечетные номера вперед, четные назад
    a5 = [1, 2, 3, 4, 5, 6, 7]
    print(f"Задание 5: Исходный={a5} => {task_5(a5)}")

    # 6. Среднее от K до L
    a6 = [4, 8, 12, 16, 20, 24]
    avg6 = task_6(a6, 2, 5)
    print(f"Задание 6: Массив={a6}, K=2, L=5 => среднее {a6[1:5]} = {avg6}")

    # 7. Арифметическая прогрессия
    p_ok = [3, 7, 11, 15, 19]
    p_no = [3, 7, 12, 15, 19]
    print(f"Задание 7: {p_ok} => разность {task_7(p_ok)}; {p_no} => {task_7(p_no)}")

    # 8. Минимум на четных позициях
    a8 = [15, 24, 7, 18, 99, 12, 30]
    print(f"Задание 8: Массив={a8} (четные: 24, 18, 12) => мин = {task_8(a8)}")

    # 9. Последний локальный максимум
    a9 = [1, 5, 3, 7, 2, 9, 4]
    print(f"Задание 9: Массив={a9} => номер последнего лок. макс = {task_9(a9)}")

    # 10. Повторяющиеся элементы
    a10 = [14, 25, 33, 42, 25, 88, 90]
    print(f"Задание 10: Массив={a10} => номера дубликатов = {task_10(a10)}")
    print("=" * 60)

if __name__ == "__main__":
    main()

def input_int(prompt, default_val):
    try:
        val = input(f"{prompt} [по умолчанию {default_val}]: ").strip()
        return int(val) if val else int(default_val)
    except (ValueError, EOFError):
        return int(default_val)

def input_float(prompt, default_val):
    try:
        val = input(f"{prompt} [по умолчанию {default_val}]: ").strip()
        return float(val) if val else float(default_val)
    except (ValueError, EOFError):
        return float(default_val)

def input_list_int(prompt, default_str):
    try:
        val = input(f"{prompt} [по умолчанию {default_str}]: ").strip()
        s = val if val else default_str
        return [int(x) for x in s.split()]
    except (ValueError, EOFError):
        return [int(x) for x in default_str.split()]

# Задача 1: N первых положительных нечетных чисел
def task_1(n: int) -> list:
    return [2 * i + 1 for i in range(n)]

# Задача 2: N членов геометрической прогрессии
def task_2(n: int, a: float, d: float) -> list:
    res = []
    curr = a
    for _ in range(n):
        res.append(curr)
        curr *= d
    return res

# Задача 3: Первые два элемента A и B, далее сумма всех предыдущих
def task_3(n: int, a: int, b: int) -> list:
    arr = [a, b]
    s = a + b
    for _ in range(2, n):
        arr.append(s)
        s += s
    return arr

# Задача 4: Чередующийся вывод: A1, AN, A2, AN-1...
def task_4(arr: list) -> list:
    res = []
    l, r = 0, len(arr) - 1
    while l <= r:
        res.append(arr[l])
        if l != r:
            res.append(arr[r])
        l += 1
        r -= 1
    return res

# Задача 5: Элементы с нечетными номерами (по возрастанию), затем с четными (по убыванию)
def task_5(arr: list) -> list:
    odd_pos = [arr[i] for i in range(0, len(arr), 2)]
    even_pos = [arr[i] for i in range(1, len(arr), 2)]
    even_pos.reverse()
    return odd_pos + even_pos

# Задача 6: Среднее арифметическое элементов с номерами от K до L (1-based)
def task_6(arr: list, k: int, l: int) -> float:
    sub = arr[k - 1:l]
    return sum(sub) / len(sub) if sub else 0.0

# Задача 7: Проверка на арифметическую прогрессию (разность или 0)
def task_7(arr: list) -> int:
    if len(arr) < 2:
        return 0
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i - 1] != diff:
            return 0
    return diff

# Задача 8: Минимальный элемент среди элементов с четными номерами (1-based)
def task_8(arr: list):
    evens = [arr[i] for i in range(1, len(arr), 2)]
    return min(evens) if evens else None

# Задача 9: Номер последнего локального максимума (1-based)
def task_9(arr: list) -> int:
    n = len(arr)
    last_idx = -1
    for i in range(n):
        l_ok = (i == 0) or (arr[i] > arr[i - 1])
        r_ok = (i == n - 1) or (arr[i] > arr[i + 1])
        if l_ok and r_ok:
            last_idx = i + 1
    return last_idx

# Задача 10: Позиции двух одинаковых элементов в порядке возрастания (1-based)
def task_10(arr: list):
    seen = {}
    for i, val in enumerate(arr, 1):
        if val in seen:
            return seen[val], i
        seen[val] = i
    return None

def run_all_demo():
    print("\n--- Демонстрационный запуск всех заданий ---")
    print(f"Задание 1 (N=7): {task_1(7)}")
    print(f"Задание 2 (N=5, A=2, D=3): {task_2(5, 2.0, 3.0)}")
    print(f"Задание 3 (N=6, A=1, B=2): {task_3(6, 1, 2)}")
    a4 = [10, 20, 30, 40, 50, 60]
    print(f"Задание 4 ({a4}): {task_4(a4)}")
    a5 = [1, 2, 3, 4, 5, 6, 7]
    print(f"Задание 5 ({a5}): {task_5(a5)}")
    a6 = [4, 8, 12, 16, 20, 24]
    print(f"Задание 6 ({a6}, K=2, L=5): {task_6(a6, 2, 5)}")
    p_ok = [3, 7, 11, 15, 19]
    print(f"Задание 7 ({p_ok}): разность = {task_7(p_ok)}")
    a8 = [15, 24, 7, 18, 99, 12, 30]
    print(f"Задание 8 ({a8}): мин на четных позициях = {task_8(a8)}")
    a9 = [1, 5, 3, 7, 2, 9, 4]
    print(f"Задание 9 ({a9}): номер последнего лок. макс = {task_9(a9)}")
    a10 = [14, 25, 33, 42, 25, 88, 90]
    print(f"Задание 10 ({a10}): номера повторов = {task_10(a10)}")

def run_interactive():
    print("\nДоступные номера задач: 1 - 10")
    try:
        choice = int(input("Введите номер задачи для проверки (1-10): ").strip())
    except (ValueError, EOFError):
        choice = 1

    if choice == 1:
        n = input_int("Размер N", 7)
        print(f"-> Массив нечетных чисел: {task_1(n)}")
    elif choice == 2:
        n = input_int("Количество N", 5)
        a = input_float("Первый член A", 2.0)
        d = input_float("Знаменатель D", 3.0)
        print(f"-> Геом. прогрессия: {task_2(n, a, d)}")
    elif choice == 3:
        n = input_int("Количество N", 6)
        a = input_int("A", 1)
        b = input_int("B", 2)
        print(f"-> Массив сумм: {task_3(n, a, b)}")
    elif choice == 4:
        arr = input_list_int("Массив через пробел", "10 20 30 40 50 60")
        print(f"-> Чередующийся вывод: {task_4(arr)}")
    elif choice == 5:
        arr = input_list_int("Массив через пробел", "1 2 3 4 5 6 7")
        print(f"-> Нечетные вперед, четные назад: {task_5(arr)}")
    elif choice == 6:
        arr = input_list_int("Массив через пробел", "4 8 12 16 20 24")
        k = input_int("K (1-based)", 2)
        l = input_int("L (1-based)", 5)
        print(f"-> Среднее элементов от {k} до {l}: {task_6(arr, k, l):.4f}")
    elif choice == 7:
        arr = input_list_int("Массив через пробел", "3 7 11 15 19")
        diff = task_7(arr)
        print(f"-> Разность прогрессии (0 если нет): {diff}")
    elif choice == 8:
        arr = input_list_int("Массив через пробел", "15 24 7 18 99 12 30")
        print(f"-> Минимум на четных позициях: {task_8(arr)}")
    elif choice == 9:
        arr = input_list_int("Массив через пробел", "1 5 3 7 2 9 4")
        print(f"-> Номер последнего локального максимума: {task_9(arr)}")
    elif choice == 10:
        arr = input_list_int("Массив с парой одинаковых чисел", "14 25 33 42 25 88 90")
        print(f"-> Номера одинаковых элементов: {task_10(arr)}")
    else:
        print("Неизвестный номер задачи.")

def main():
    print("=" * 60)
    print("Лабораторная работа №5: Одномерные массивы")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    print("\nВыберите режим работы:")
    print("1 - Запустить авто-демонстрацию всех задач")
    print("2 - Ввести свои данные для конкретной задачи")
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

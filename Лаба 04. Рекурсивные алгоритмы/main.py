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

def input_str(prompt, default_val):
    try:
        val = input(f"{prompt} [по умолчанию '{default_val}']: ").strip()
        return val if val else default_val
    except (ValueError, EOFError):
        return default_val

# Задача 1: Рекурсивный факториал числа
def factorial(n: int) -> int:
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# Задача 2: Рекурсивное число Фибоначчи
def fibonacci(n: int) -> int:
    if n <= 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

# Задача 3: Рекурсивное быстрое возведение в степень
def power(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    if n < 0:
        return 1.0 / power(x, -n)
    if n % 2 == 0:
        h = power(x, n // 2)
        return h * h
    return x * power(x, n - 1)

# Задача 4: Рекурсивная проверка на палиндром
def is_palindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    def _chk(t):
        if len(t) <= 1:
            return True
        if t[0] != t[-1]:
            return False
        return _chk(t[1:-1])
    return _chk(cleaned)

# Задача 5: Рекурсивный бинарный поиск
def binary_search_rec(arr: list, target, left: int = 0, right: int = None) -> int:
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_rec(arr, target, left, mid - 1)
    else:
        return binary_search_rec(arr, target, mid + 1, right)

# Задача 6: Рекурсивный обратный порядок слов
def reverse_words_rec(s: str) -> str:
    s = s.strip()
    if " " not in s:
        return s
    first, rest = s.split(" ", 1)
    return reverse_words_rec(rest) + " " + first

# Вспомогательная проверка простоты числа
def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Задача 7: Разложение числа на сумму простых чисел
def prime_sum_decomposition(n: int, min_p: int = 2):
    if n == 0:
        return []
    if n < 2:
        return None
    for p in range(min_p, n + 1):
        if is_prime(p):
            sub = prime_sum_decomposition(n - p, p)
            if sub is not None:
                return [p] + sub
    return None

# Задача 8: Рекурсивный подсчет количества цифр
def count_digits(n: int) -> int:
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

# Задача 9: Ханойская башня
def hanoi_towers(n: int, src: str, dst: str, aux: str, moves: list = None) -> list:
    if moves is None:
        moves = []
    if n == 1:
        moves.append(f"Диск 1 со стержня {src} на {dst}")
        return moves
    hanoi_towers(n - 1, src, aux, dst, moves)
    moves.append(f"Диск {n} со стержня {src} на {dst}")
    hanoi_towers(n - 1, aux, dst, src, moves)
    return moves

def run_all_demo():
    print("\n--- Демонстрационный запуск всех заданий ---")
    print(f"Задание 1: 5! = {factorial(5)}, 7! = {factorial(7)}")
    print(f"Задание 2: Первые 8 чисел Фибоначчи: {[fibonacci(i) for i in range(1, 9)]}")
    print(f"Задание 3: 2^8 = {power(2, 8)}")
    print(f"Задание 4: «А роза упала на лапу Азора» -> {is_palindrome('А роза упала на лапу Азора')}")
    arr = [10, 20, 30, 40, 50, 60]
    print(f"Задание 5: Поиск 40 в {arr} -> индекс {binary_search_rec(arr, 40)}")
    text = "студент изучает алгоритмы"
    print(f"Задание 6: «{text}» -> «{reverse_words_rec(text)}»")
    print(f"Задание 7: Разложение 28 -> {' + '.join(map(str, prime_sum_decomposition(28)))}")
    print(f"Задание 8: Цифр в числе 1048576 = {count_digits(1048576)}")
    print(f"Задание 9: Ханойская башня для 3 дисков ({len(hanoi_towers(3, 'A', 'C', 'B'))} ходов)")

def run_interactive():
    print("\nДоступные номера задач: 1 - 9")
    try:
        choice = int(input("Введите номер задачи для проверки (1-9): ").strip())
    except (ValueError, EOFError):
        choice = 1

    if choice == 1:
        n = input_int("Введите число n", 5)
        print(f"-> Факториал {n}! = {factorial(n)}")
    elif choice == 2:
        n = input_int("Номер числа Фибоначчи n", 8)
        print(f"-> {n}-е число Фибоначчи = {fibonacci(n)}")
    elif choice == 3:
        x = input_float("Число x", 2.0)
        n = input_int("Степень n", 8)
        print(f"-> {x}^{n} = {power(x, n)}")
    elif choice == 4:
        s = input_str("Строка для проверки", "А роза упала на лапу Азора")
        res = "палиндром" if is_palindrome(s) else "НЕ палиндром"
        print(f"-> Строка «{s}» — это {res}")
    elif choice == 5:
        raw = input_str("Отсортированный массив через пробел", "10 23 35 42 56 78")
        arr = [int(x) for x in raw.split()]
        target = input_int("Искомый элемент", 42)
        idx = binary_search_rec(arr, target)
        print(f"-> Индекс элемента {target}: {idx}")
    elif choice == 6:
        s = input_str("Строка со словами", "студент изучает линейные алгоритмы")
        print(f"-> Обратный порядок: «{reverse_words_rec(s)}»")
    elif choice == 7:
        n = input_int("Число для разложения (> 1)", 28)
        decomp = prime_sum_decomposition(n)
        if decomp:
            print(f"-> Разложение {n} = {' + '.join(map(str, decomp))}")
        else:
            print("-> Не удалось разложить.")
    elif choice == 8:
        n = input_int("Число для подсчета цифр", 1048576)
        print(f"-> Количество цифр: {count_digits(n)}")
    elif choice == 9:
        n = input_int("Количество дисков (1-6)", 3)
        moves = hanoi_towers(n, "A", "C", "B")
        print(f"-> Перемещение {n} дисков ({len(moves)} ходов):")
        for i, m in enumerate(moves, 1):
            print(f"  {i}. {m}")
    else:
        print("Неизвестный номер задачи.")

def main():
    print("=" * 60)
    print("Лабораторная работа №4: Рекурсивные алгоритмы")
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

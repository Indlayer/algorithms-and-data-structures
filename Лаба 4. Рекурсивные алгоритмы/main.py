def factorial(n: int) -> int:
    """Задача 1: Рекурсивное вычисление факториала n!"""
    if n < 0:
        raise ValueError("Факториал определен только для неотрицательных чисел")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n: int) -> int:
    """Задача 2: Рекурсивное вычисление n-го числа Фибоначчи (1, 1, 2, 3, 5, 8...)."""
    if n <= 0:
        raise ValueError("Номер числа Фибоначчи должен быть натуральным числом")
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def power(x: float, n: int) -> float:
    """Задача 3: Рекурсивное возведение x в целую степень n."""
    if n == 0:
        return 1.0
    if n < 0:
        return 1.0 / power(x, -n)
    if n % 2 == 0:
        half = power(x, n // 2)
        return half * half
    return x * power(x, n - 1)

def is_palindrome(s: str) -> bool:
    """Задача 4: Рекурсивная проверка строки на палиндром."""
    # Приводим к нижнему регистру и убираем пробелы
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    
    def _helper(text: str) -> bool:
        if len(text) <= 1:
            return True
        if text[0] != text[-1]:
            return False
        return _helper(text[1:-1])
        
    return _helper(cleaned)

def binary_search_rec(arr: list, target, left: int = 0, right: int = None) -> int:
    """Задача 5: Рекурсивный бинарный поиск элемента в отсортированном массиве."""
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1  # Элемент не найден
    
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_rec(arr, target, left, mid - 1)
    else:
        return binary_search_rec(arr, target, mid + 1, right)

def reverse_words_rec(s: str) -> str:
    """Задача 6: Рекурсивное изменение порядка слов в строке на обратный."""
    s = s.strip()
    if not s:
        return ""
    if " " not in s:
        return s
    first, rest = s.split(" ", 1)
    return reverse_words_rec(rest) + " " + first

def is_prime(num: int) -> bool:
    """Вспомогательная проверка простоты числа."""
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_sum_decomposition(n: int, min_prime: int = 2):
    """Задача 7: Рекурсивное разложение числа на сумму простых чисел."""
    if n == 0:
        return []
    if n < 2:
        return None
    
    for p in range(min_prime, n + 1):
        if is_prime(p):
            sub_res = prime_sum_decomposition(n - p, p)
            if sub_res is not None:
                return [p] + sub_res
    return None

def count_digits(n: int) -> int:
    """Задача 8: Рекурсивный подсчет количества цифр в числе."""
    n = abs(n)
    if n < 10:
        return 1
    return 1 + count_digits(n // 10)

def hanoi_towers(n: int, source: str, target: str, auxiliary: str, moves: list = None) -> list:
    """Задача 9: Рекурсивное решение головоломки 'Ханойская башня'."""
    if moves is None:
        moves = []
    if n == 1:
        moves.append(f"Переместить диск 1 со стержня {source} на {target}")
        return moves
    # Перемещаем n-1 дисков с source на auxiliary
    hanoi_towers(n - 1, source, auxiliary, target, moves)
    # Перемещаем 1 оставшийся диск с source на target
    moves.append(f"Переместить диск {n} со стержня {source} на {target}")
    # Перемещаем n-1 дисков с auxiliary на target
    hanoi_towers(n - 1, auxiliary, target, source, moves)
    return moves

def main():
    print("=" * 60)
    print("Лабораторная работа №4: Рекурсивные алгоритмы")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    # 1. Факториал
    print(f"Задание 1: 5! = {factorial(5)}; 7! = {factorial(7)}")

    # 2. Фибоначчи
    fib_series = [fibonacci(i) for i in range(1, 10)]
    print(f"Задание 2: Первые 9 чисел Фибоначчи = {fib_series}")

    # 3. Возведение в степень
    print(f"Задание 3: 2^8 = {power(2, 8)}; 3^(-2) = {power(3, -2)}")

    # 4. Палиндром
    s1 = "А роза упала на лапу Азора"
    s2 = "Алгоритмы"
    print(f"Задание 4: «{s1}» => {is_palindrome(s1)}; «{s2}» => {is_palindrome(s2)}")

    # 5. Рекурсивный бинарный поиск
    data = [10, 23, 35, 42, 56, 67, 78, 89, 99]
    idx = binary_search_rec(data, 56)
    print(f"Задание 5: Массив={data}, ищем 56 => индекс {idx}")

    # 6. Обратный порядок слов
    text = "студент изучает линейные алгоритмы и структуры"
    print(f"Задание 6: Исходная: «{text}»\n           Обратная: «{reverse_words_rec(text)}»")

    # 7. Разложение на простые числа
    num_to_decomp = 28
    decomp = prime_sum_decomposition(num_to_decomp)
    print(f"Задание 7: Разложение {num_to_decomp} на простые слагаемые: {' + '.join(map(str, decomp))} = {num_to_decomp}")

    # 8. Количество цифр
    n_digits = 1048576
    print(f"Задание 8: Количество цифр в числе {n_digits} = {count_digits(n_digits)}")

    # 9. Ханойская башня для 3 дисков
    print("Задание 9: Ханойская башня для 3 дисков (стержни A -> C с исп. B):")
    moves = hanoi_towers(3, "A", "C", "B")
    for i, m in enumerate(moves, 1):
        print(f"  {i}. {m}")
    print("=" * 60)

if __name__ == "__main__":
    main()

def input_float(prompt, default_val):
    try:
        val = input(f"{prompt} [по умолчанию {default_val}]: ").strip()
        return float(val) if val else float(default_val)
    except (ValueError, EOFError):
        return float(default_val)

def input_int(prompt, default_val):
    try:
        val = input(f"{prompt} [по умолчанию {default_val}]: ").strip()
        return int(val) if val else int(default_val)
    except (ValueError, EOFError):
        return int(default_val)

# Задача 1: Стоимость от 0.1 до 1.0 кг конфет
def task_1(price_per_kg: float):
    return [(i / 10.0, round(i / 10.0 * price_per_kg, 2)) for i in range(1, 11)]

# Задача 2: Произведение 1.1 * 1.2 * ... (N сомножителей)
def task_2(n: int):
    prod = 1.0
    for i in range(1, n + 1):
        prod *= (1.0 + i * 0.1)
    return prod

# Задача 3: Квадрат числа через сумму нечетных с выводом промежуточных сумм
def task_3(n: int):
    curr = 0
    history = []
    for i in range(1, n + 1):
        odd = 2 * i - 1
        curr += odd
        history.append((odd, curr))
    return curr, history

# Задача 4: Сумма степеней 1 + A + A^2 + ... + A^N
def task_4(a: float, n: int):
    total = 1.0
    term = 1.0
    for _ in range(n):
        term *= a
        total += term
    return total

# Задача 5: Знакопеременная сумма (без оператора if)
def task_5(a: float, n: int):
    total = 1.0
    term = 1.0
    mult = -a
    for _ in range(n):
        term *= mult
        total += term
    return total

# Задача 6: Вывод чисел от A до B с повторением
def task_6(a: int, b: int):
    res = []
    for num in range(a, b + 1):
        for _ in range(num):
            res.append(num)
    return res

# Задача 7: Отрезки без умножения и деления (только вычитание)
def task_7(a: float, b: float):
    rem = a
    while rem >= b:
        rem -= b
    return rem

# Задача 8: Наименьшее K для суммы 1 + 2 + ... + K >= N
def task_8(n: int):
    curr = 0
    k = 0
    while curr < n:
        k += 1
        curr += k
    return k, curr

# Задача 9: Банковский вклад (1000 руб, рост на P% в месяц до 1100 руб)
def task_9(p: float):
    deposit = 1000.0
    months = 0
    rate = p / 100.0
    while deposit <= 1100.0:
        months += 1
        deposit += deposit * rate
    return months, round(deposit, 2)

# Задача 10: НОД алгоритмом Евклида
def task_10(a: int, b: int):
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    return x

def run_all_demo():
    print("\n--- Демонстрационный запуск всех заданий ---")
    print("Задание 1 (цена 450 руб/кг):")
    for w, c in task_1(450.0)[:3]:
        print(f"  {w:.1f} кг = {c:.2f} руб.")
    print("  ...")
    print(f"Задание 2 (N=5): Произведение = {task_2(5):.6f}")
    sq, _ = task_3(5)
    print(f"Задание 3 (N=5): 5^2 = {sq}")
    print(f"Задание 4 (A=2, N=4): 1 + 2 + 4 + 8 + 16 = {task_4(2.0, 4)}")
    print(f"Задание 5 (A=2, N=4): 1 - 2 + 4 - 8 + 16 = {task_5(2.0, 4)}")
    print(f"Задание 6 (A=2, B=4): {task_6(2, 4)}")
    print(f"Задание 7 (A=14.5, B=3.0): Остаток = {task_7(14.5, 3.0):.2f}")
    k8, s8 = task_8(15)
    print(f"Задание 8 (N=15): K = {k8}, Сумма = {s8}")
    m9, s9 = task_9(3.5)
    print(f"Задание 9 (P=3.5%): Месяцев = {m9}, Итого = {s9} руб.")
    print(f"Задание 10 (НОД(140, 96)): {task_10(140, 96)}")

def run_interactive():
    print("\nДоступные номера задач: 1 - 10")
    try:
        choice = int(input("Введите номер задачи для проверки (1-10): ").strip())
    except (ValueError, EOFError):
        choice = 1

    if choice == 1:
        price = input_float("Цена за 1 кг конфет", 450.0)
        print("-> Стоимость:")
        for w, c in task_1(price):
            print(f"  {w:.1f} кг = {c:.2f} руб.")
    elif choice == 2:
        n = input_int("Число сомножителей N", 5)
        print(f"-> Произведение = {task_2(n):.6f}")
    elif choice == 3:
        n = input_int("Число N (> 0)", 5)
        sq, hist = task_3(n)
        print(f"-> Квадрат N^2 = {sq}")
        for odd, s in hist:
            print(f"  + {odd} => текущая сумма = {s}")
    elif choice == 4:
        a = input_float("Число A", 2.0)
        n = input_int("Степень N", 4)
        print(f"-> Сумма 1 + A + ... + A^N = {task_4(a, n)}")
    elif choice == 5:
        a = input_float("Число A", 2.0)
        n = input_int("Степень N", 4)
        print(f"-> Знакопеременная сумма (без if) = {task_5(a, n)}")
    elif choice == 6:
        a = input_int("Число A", 2)
        b = input_int("Число B (> A)", 4)
        print(f"-> Последовательность: {task_6(a, b)}")
    elif choice == 7:
        a = input_float("Длина отрезка A", 14.5)
        b = input_float("Длина отрезка B (< A)", 3.0)
        print(f"-> Длина незанятой части = {task_7(a, b):.4f}")
    elif choice == 8:
        n = input_int("Число N (> 1)", 15)
        k, s = task_8(n)
        print(f"-> Наименьшее K = {k}, сумма = {s}")
    elif choice == 9:
        p = input_float("Процент P (0 < P < 25)", 3.5)
        m, s = task_9(p)
        print(f"-> Превысит 1100 руб через {m} месяцев (сумма: {s} руб)")
    elif choice == 10:
        a = input_int("Число A", 140)
        b = input_int("Число B", 96)
        print(f"-> НОД({a}, {b}) = {task_10(a, b)}")
    else:
        print("Неизвестный номер задачи.")

def main():
    print("=" * 60)
    print("Лабораторная работа №3: Циклические алгоритмы")
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

import math

# Вспомогательная функция для безопасного ввода чисел
def input_float(prompt, default_val):
    try:
        val = input(f"{prompt} [по умолчанию {default_val}]: ").strip()
        if not val:
            return float(default_val)
        return float(val)
    except (ValueError, EOFError):
        return float(default_val)

# Задача 1: Стороны прямоугольника a и b
def task_1(a: float, b: float):
    s = a * b
    p = 2 * (a + b)
    return s, p

# Задача 2: Длина окружности по диаметру
def task_2(d: float):
    pi = 3.14
    return pi * d

# Задача 3: Среднее арифметическое двух чисел
def task_3(a: float, b: float):
    return (a + b) / 2

# Задача 4: Операции над квадратами двух ненулевых чисел
def task_4(a: float, b: float):
    if a == 0 or b == 0:
        raise ValueError("Числа не должны быть равны нулю!")
    sq_a = a ** 2
    sq_b = b ** 2
    return sq_a + sq_b, sq_a - sq_b, sq_a * sq_b, sq_a / sq_b

# Задача 5: Операции над модулями двух ненулевых чисел
def task_5(a: float, b: float):
    if a == 0 or b == 0:
        raise ValueError("Числа не должны быть равны нулю!")
    abs_a = abs(a)
    abs_b = abs(b)
    return abs_a + abs_b, abs_a - abs_b, abs_a * abs_b, abs_a / abs_b

# Задача 6: Расстояние между двумя точками
def task_6(x1: float, y1: float, x2: float, y2: float):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Задача 7: Отрезки AC и BC на числовой оси
def task_7(a: float, b: float, c: float):
    ac = abs(a - c)
    bc = abs(b - c)
    return ac, bc, ac + bc

# Задача 8: Произведение отрезков AC и BC (точка C между A и B)
def task_8(a: float, b: float, c: float):
    ac = abs(c - a)
    bc = abs(b - c)
    return ac * bc

# Задача 9: Периметр и площадь прямоугольника по двум противоположным вершинам
def task_9(x1: float, y1: float, x2: float, y2: float):
    w = abs(x2 - x1)
    h = abs(y2 - y1)
    return 2 * (w + h), w * h

# Задача 10: Периметр и площадь треугольника (формула Герона)
def task_10(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    p = a + b + c
    hp = p / 2
    s = math.sqrt(hp * (hp - a) * (hp - b) * (hp - c))
    return p, s

# Задача 11: Функция y = 3x^6 - 6x^2 - 7
def task_11(x: float):
    return 3 * (x ** 6) - 6 * (x ** 2) - 7

# Задача 12: Функция y = 4(x-3)^6 - 7(x-3)^3 + 2
def task_12(x: float):
    d = x - 3
    return 4 * (d ** 6) - 7 * (d ** 3) + 2

# Автоматический запуск всех задач с демонстрационными данными
def run_all_demo():
    print("\n--- Демонстрационный запуск всех заданий ---")
    s1, p1 = task_1(4.0, 5.0)
    print(f"Задание 1 (a=4, b=5): Площадь={s1}, Периметр={p1}")

    l2 = task_2(10.0)
    print(f"Задание 2 (d=10): Длина окружности={l2:.2f}")

    avg3 = task_3(7.0, 13.0)
    print(f"Задание 3 (a=7, b=13): Среднее={avg3}")

    sum4, diff4, mul4, div4 = task_4(4.0, 2.0)
    print(f"Задание 4 (a=4, b=2): Квадраты: сумма={sum4}, разность={diff4}, произв={mul4}, частное={div4}")

    sum5, diff5, mul5, div5 = task_5(-5.0, 2.5)
    print(f"Задание 5 (a=-5, b=2.5): Модули: сумма={sum5}, разность={diff5}, произв={mul5}, частное={div5}")

    dist6 = task_6(1.0, 1.0, 4.0, 5.0)
    print(f"Задание 6 (A(1,1), B(4,5)): Расстояние={dist6:.4f}")

    ac7, bc7, sum7 = task_7(2.0, 10.0, 5.0)
    print(f"Задание 7 (A=2, B=10, C=5): AC={ac7}, BC={bc7}, Сумма={sum7}")

    prod8 = task_8(1.0, 9.0, 4.0)
    print(f"Задание 8 (A=1, B=9, C=4): AC*BC={prod8}")

    p9, s9 = task_9(1.0, 2.0, 6.0, 5.0)
    print(f"Задание 9 ((1,2), (6,5)): Периметр={p9}, Площадь={s9}")

    p10, s10 = task_10(0.0, 0.0, 4.0, 0.0, 0.0, 3.0)
    print(f"Задание 10 ((0,0), (4,0), (0,3)): Периметр={p10:.4f}, Площадь={s10:.4f}")

    y11 = task_11(2.0)
    print(f"Задание 11 (x=2): y={y11}")

    y12 = task_12(4.0)
    print(f"Задание 12 (x=4): y={y12}")

# Интерактивный ввод данных для выбранной задачи
def run_interactive():
    print("\nДоступные номера задач: 1 - 12")
    try:
        choice = int(input("Введите номер задачи для проверки (1-12): ").strip())
    except (ValueError, EOFError):
        choice = 1

    if choice == 1:
        a = input_float("Введите сторону a", 4.0)
        b = input_float("Введите сторону b", 5.0)
        s, p = task_1(a, b)
        print(f"-> Результат: Площадь S = {s}, Периметр P = {p}")
    elif choice == 2:
        d = input_float("Введите диаметр d", 10.0)
        print(f"-> Результат: Длина окружности L = {task_2(d):.4f}")
    elif choice == 3:
        a = input_float("Введите число a", 7.0)
        b = input_float("Введите число b", 13.0)
        print(f"-> Результат: Среднее арифметическое = {task_3(a, b)}")
    elif choice == 4:
        a = input_float("Введите число a (не 0)", 4.0)
        b = input_float("Введите число b (не 0)", 2.0)
        s, d, m, div = task_4(a, b)
        print(f"-> Квадраты: сумма={s}, разность={d}, произв={m}, частное={div}")
    elif choice == 5:
        a = input_float("Введите число a (не 0)", -5.0)
        b = input_float("Введите число b (не 0)", 2.5)
        s, d, m, div = task_5(a, b)
        print(f"-> Модули: сумма={s}, разность={d}, произв={m}, частное={div}")
    elif choice == 6:
        x1 = input_float("Введите x1", 1.0)
        y1 = input_float("Введите y1", 1.0)
        x2 = input_float("Введите x2", 4.0)
        y2 = input_float("Введите y2", 5.0)
        print(f"-> Расстояние = {task_6(x1, y1, x2, y2):.4f}")
    elif choice == 7:
        a = input_float("Точка A", 2.0)
        b = input_float("Точка B", 10.0)
        c = input_float("Точка C", 5.0)
        ac, bc, sm = task_7(a, b, c)
        print(f"-> AC = {ac}, BC = {bc}, Сумма = {sm}")
    elif choice == 8:
        a = input_float("Точка A", 1.0)
        b = input_float("Точка B", 9.0)
        c = input_float("Точка C (между A и B)", 4.0)
        print(f"-> Произведение AC * BC = {task_8(a, b, c)}")
    elif choice == 9:
        x1 = input_float("x1", 1.0)
        y1 = input_float("y1", 2.0)
        x2 = input_float("x2", 6.0)
        y2 = input_float("y2", 5.0)
        p, s = task_9(x1, y1, x2, y2)
        print(f"-> Периметр = {p}, Площадь = {s}")
    elif choice == 10:
        x1, y1 = input_float("x1", 0.0), input_float("y1", 0.0)
        x2, y2 = input_float("x2", 4.0), input_float("y2", 0.0)
        x3, y3 = input_float("x3", 0.0), input_float("y3", 3.0)
        p, s = task_10(x1, y1, x2, y2, x3, y3)
        print(f"-> Периметр = {p:.4f}, Площадь = {s:.4f}")
    elif choice == 11:
        x = input_float("Введите x", 2.0)
        print(f"-> y = 3x^6 - 6x^2 - 7 = {task_11(x)}")
    elif choice == 12:
        x = input_float("Введите x", 4.0)
        print(f"-> y = 4(x-3)^6 - 7(x-3)^3 + 2 = {task_12(x)}")
    else:
        print("Неизвестный номер задачи.")

def main():
    print("=" * 60)
    print("Лабораторная работа №1: Линейные алгоритмы")
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

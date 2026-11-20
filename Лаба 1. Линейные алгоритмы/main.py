import math

def task_1(a: float, b: float):
    """Задача 1: Стороны прямоугольника a и b. Найти площадь S = a*b и периметр P = 2*(a+b)."""
    s = a * b
    p = 2 * (a + b)
    return s, p

def task_2(d: float):
    """Задача 2: Диаметр окружности d. Найти ее длину L = pi*d (pi = 3.14)."""
    pi = 3.14
    length = pi * d
    return length

def task_3(a: float, b: float):
    """Задача 3: Найти среднее арифметическое двух чисел (a + b) / 2."""
    return (a + b) / 2

def task_4(a: float, b: float):
    """Задача 4: Два ненулевых числа. Сумма, разность, произведение и частное их квадратов."""
    if a == 0 or b == 0:
        raise ValueError("Числа должны быть ненулевыми!")
    sq_a = a ** 2
    sq_b = b ** 2
    return sq_a + sq_b, sq_a - sq_b, sq_a * sq_b, sq_a / sq_b

def task_5(a: float, b: float):
    """Задача 5: Два ненулевых числа. Сумма, разность, произведение и частное их модулей."""
    if a == 0 or b == 0:
        raise ValueError("Числа должны быть ненулевыми!")
    abs_a = abs(a)
    abs_b = abs(b)
    return abs_a + abs_b, abs_a - abs_b, abs_a * abs_b, abs_a / abs_b

def task_6(x1: float, y1: float, x2: float, y2: float):
    """Задача 6: Расстояние между двумя точками (x1, y1) и (x2, y2)."""
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def task_7(a: float, b: float, c: float):
    """Задача 7: Три точки A, B, C на числовой оси. Длины AC, BC и их сумма."""
    ac = abs(a - c)
    bc = abs(b - c)
    return ac, bc, ac + bc

def task_8(a: float, b: float, c: float):
    """Задача 8: Три точки A, B, C на оси (C между A и B). Произведение длин отрезков AC и BC."""
    ac = abs(c - a)
    bc = abs(b - c)
    return ac * bc

def task_9(x1: float, y1: float, x2: float, y2: float):
    """Задача 9: Противоположные вершины прямоугольника со сторонами parallel осям. Периметр и площадь."""
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    p = 2 * (width + height)
    s = width * height
    return p, s

def task_10(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float):
    """Задача 10: Координаты трех вершин треугольника. Периметр и площадь (формула Герона)."""
    a = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    b = math.sqrt((x3 - x2) ** 2 + (y3 - y2) ** 2)
    c = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    p = a + b + c
    half_p = p / 2
    s = math.sqrt(half_p * (half_p - a) * (half_p - b) * (half_p - c))
    return p, s

def task_11(x: float):
    """Задача 11: Значение функции y = 3*x^6 - 6*x^2 - 7."""
    return 3 * (x ** 6) - 6 * (x ** 2) - 7

def task_12(x: float):
    """Задача 12: Значение функции y = 4*(x-3)^6 - 7*(x-3)^3 + 2."""
    diff = x - 3
    return 4 * (diff ** 6) - 7 * (diff ** 3) + 2

def main():
    print("=" * 60)
    print("Лабораторная работа №1: Линейные алгоритмы")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    # 1. Прямоугольник
    s1, p1 = task_1(4.0, 5.0)
    print(f"Задание 1: a=4, b=5 => Площадь S = {s1}, Периметр P = {p1}")

    # 2. Окружность
    l2 = task_2(10.0)
    print(f"Задание 2: d=10 => Длина окружности L = {l2}")

    # 3. Среднее арифметическое
    avg3 = task_3(7.0, 13.0)
    print(f"Задание 3: a=7, b=13 => Среднее арифметическое = {avg3}")

    # 4. Операции с квадратами
    sum4, diff4, mul4, div4 = task_4(4.0, 2.0)
    print(f"Задание 4: a=4, b=2 => Квадраты (16 и 4): сумма={sum4}, разность={diff4}, произв={mul4}, частное={div4}")

    # 5. Операции с модулями
    sum5, diff5, mul5, div5 = task_5(-5.0, 2.5)
    print(f"Задание 5: a=-5, b=2.5 => Модули (5.0 и 2.5): сумма={sum5}, разность={diff5}, произв={mul5}, частное={div5}")

    # 6. Расстояние между точками
    dist6 = task_6(1.0, 1.0, 4.0, 5.0)
    print(f"Задание 6: A(1,1), B(4,5) => Расстояние = {dist6:.4f}")

    # 7. Точки на оси
    ac7, bc7, sum7 = task_7(2.0, 10.0, 5.0)
    print(f"Задание 7: A=2, B=10, C=5 => AC={ac7}, BC={bc7}, Сумма={sum7}")

    # 8. Точка между A и B
    prod8 = task_8(1.0, 9.0, 4.0)
    print(f"Задание 8: A=1, B=9, C=4 => Произведение AC*BC = {prod8}")

    # 9. Прямоугольник по координатам вершин
    p9, s9 = task_9(1.0, 2.0, 6.0, 5.0)
    print(f"Задание 9: (1,2) и (6,5) => Периметр = {p9}, Площадь = {s9}")

    # 10. Треугольник по координатам вершин
    p10, s10 = task_10(0.0, 0.0, 4.0, 0.0, 0.0, 3.0)
    print(f"Задание 10: (0,0), (4,0), (0,3) => Периметр = {p10:.4f}, Площадь = {s10:.4f}")

    # 11. Вычисление функции y = 3x^6 - 6x^2 - 7
    y11 = task_11(2.0)
    print(f"Задание 11: x=2 => y = 3*(2^6) - 6*(2^2) - 7 = {y11}")

    # 12. Вычисление функции y = 4(x-3)^6 - 7(x-3)^3 + 2
    y12 = task_12(4.0)
    print(f"Задание 12: x=4 => y = 4*(1^6) - 7*(1^3) + 2 = {y12}")
    print("=" * 60)

if __name__ == "__main__":
    main()

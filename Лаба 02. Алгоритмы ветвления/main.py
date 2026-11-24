import math

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

# Задача 1: Если A != B, присвоить max(A, B), иначе 0
def task_1(a: int, b: int):
    if a != b:
        val = max(a, b)
        return val, val
    return 0, 0

# Задача 2: Сумма двух наибольших из трех чисел
def task_2(a: float, b: float, c: float):
    return (a + b + c) - min(a, b, c)

# Задача 3: Какая из точек B или C ближе к A
def task_3(xa: float, ya: float, xb: float, yb: float, xc: float, yc: float):
    dist_b = math.sqrt((xb - xa) ** 2 + (yb - ya) ** 2)
    dist_c = math.sqrt((xc - xa) ** 2 + (yc - ya) ** 2)
    if dist_b < dist_c:
        return "B", (xb, yb), dist_b
    elif dist_c < dist_b:
        return "C", (xc, yc), dist_c
    return "Равноудалены", ((xb, yb), (xc, yc)), dist_b

# Задача 4: Определение координатной четверти
def task_4(x: float, y: float):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4
    return 0

# Задача 5: Описание целого числа
def task_5(n: int):
    if n == 0:
        return "нулевое число"
    sign = "положительное" if n > 0 else "отрицательное"
    parity = "четное" if n % 2 == 0 else "нечетное"
    return f"{sign} {parity} число"

# Задача 6: Описание числа 1-999
def task_6(n: int):
    if not (1 <= n <= 999):
        return "число вне диапазона 1-999"
    parity = "четное" if n % 2 == 0 else "нечетное"
    if n < 10:
        digits = "однозначное"
    elif n < 100:
        digits = "двузначное"
    else:
        digits = "трехзначное"
    return f"{parity} {digits} число"

# Задача 7: Дата прописью
def task_7(day: int, month: int):
    months = [
        "января", "февраля", "марта", "апреля", "мая", "июня",
        "июля", "августа", "сентября", "октября", "ноября", "декабря"
    ]
    days = {
        1: "первое", 2: "второе", 3: "третье", 4: "четвертое", 5: "пятое",
        6: "шестое", 7: "седьмое", 8: "восьмое", 9: "девятое", 10: "десятое",
        11: "одиннадцатое", 12: "двенадцатое", 13: "тринадцатое", 14: "четырнадцатое", 15: "пятнадцатое",
        16: "шестнадцатое", 17: "семнадцатое", 18: "восемнадцатое", 19: "девятнадцатое", 20: "двадцатое",
        21: "двадцать первое", 22: "двадцать второе", 23: "двадцать третье", 24: "двадцать четвертое",
        25: "двадцать пятое", 26: "двадцать шестое", 27: "двадцать седьмое", 28: "двадцать восьмое",
        29: "двадцать девятое", 30: "тридцатое", 31: "тридцать первое"
    }
    if not (1 <= month <= 12) or not (1 <= day <= 31):
        return "некорректная дата"
    return f"{days.get(day, str(day))} {months[month - 1]}"

# Задача 8: Согласование со словами «учебное задание»
def task_8(n: int):
    if not (10 <= n <= 40):
        return "число вне диапазона 10-40"
    words_10_19 = {
        10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать",
        15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"
    }
    tens = {2: "двадцать", 3: "тридцать", 4: "сорок"}
    units = {1: "одно", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять"}

    if 10 <= n <= 19:
        num_str = words_10_19[n]
        form = "учебных заданий"
    elif n == 40:
        num_str = "сорок"
        form = "учебных заданий"
    else:
        t = n // 10
        u = n % 10
        if u == 0:
            num_str = tens[t]
            form = "учебных заданий"
        else:
            num_str = f"{tens[t]} {units[u]}"
            if u == 1:
                form = "учебное задание"
            elif 2 <= u <= 4:
                form = "учебных задания"
            else:
                form = "учебных заданий"
    return f"{num_str} {form}"

# Задача 9: Число 100-999 словами
def task_9(n: int):
    if not (100 <= n <= 999):
        return "число вне диапазона 100-999"
    hundreds = {
        1: "сто", 2: "двести", 3: "триста", 4: "четыреста", 5: "пятьсот",
        6: "шестьсот", 7: "семьсот", 8: "восемьсот", 9: "девятьсот"
    }
    tens = {
        2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят",
        6: "шестьдесят", 7: "семьдесят", 8: "восемьдесят", 9: "девяносто"
    }
    teens = {
        10: "десять", 11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать",
        15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"
    }
    units = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять", 6: "шесть", 7: "семь", 8: "восемь", 9: "девять"}

    h = n // 100
    rem = n % 100
    t = rem // 10
    u = rem % 10

    parts = [hundreds[h]]
    if 10 <= rem <= 19:
        parts.append(teens[rem])
    else:
        if t > 0:
            parts.append(tens[t])
        if u > 0:
            parts.append(units[u])
    return " ".join(parts)

# Задача 10: Восточный календарь
def task_10(year: int):
    diff = (year - 1984) % 60
    subcycle = diff // 12
    animal_idx = diff % 12
    animals = [
        ("крысы", "f"), ("коровы", "f"), ("тигра", "m"), ("зайца", "m"),
        ("дракона", "m"), ("змеи", "f"), ("лошади", "f"), ("овцы", "f"),
        ("обезьяны", "f"), ("курицы", "f"), ("собаки", "f"), ("свиньи", "f")
    ]
    colors = [
        {"m": "зеленого", "f": "зеленой"},
        {"m": "красного", "f": "красной"},
        {"m": "желтого", "f": "желтой"},
        {"m": "белого", "f": "белой"},
        {"m": "черного", "f": "черной"}
    ]
    animal_gen, gender = animals[animal_idx]
    color_str = colors[subcycle][gender]
    return f"год {color_str} {animal_gen}"

def run_all_demo():
    print("\n--- Демонстрационный запуск всех заданий ---")
    print(f"Задание 1 (A=5, B=12): {task_1(5, 12)}")
    print(f"Задание 2 (12, 35, 24): Сумма двух наибольших = {task_2(12, 35, 24)}")
    pt, c, d = task_3(0, 0, 3, 4, 1, 1)
    print(f"Задание 3 (A(0,0), B(3,4), C(1,1)): Ближе {pt} ({d:.4f})")
    print(f"Задание 4 ((-3, 5)): {task_4(-3, 5)}-я четверть")
    print(f"Задание 5 (-8, 15): -8 -> «{task_5(-8)}», 15 -> «{task_5(15)}»")
    print(f"Задание 6 (42, 105): 42 -> «{task_6(42)}», 105 -> «{task_6(105)}»")
    print(f"Задание 7 (5 января): «{task_7(5, 1)}»")
    print(f"Задание 8 (18, 21): 18 -> «{task_8(18)}», 21 -> «{task_8(21)}»")
    print(f"Задание 9 (256): «{task_9(256)}»")
    print(f"Задание 10 (1984, 2026): 1984 -> «{task_10(1984)}», 2026 -> «{task_10(2026)}»")

def run_interactive():
    print("\nДоступные номера задач: 1 - 10")
    try:
        choice = int(input("Введите номер задачи для проверки (1-10): ").strip())
    except (ValueError, EOFError):
        choice = 1

    if choice == 1:
        a = input_int("Введите целое A", 5)
        b = input_int("Введите целое B", 12)
        print(f"-> Результат: {task_1(a, b)}")
    elif choice == 2:
        a = input_float("Число a", 12.0)
        b = input_float("Число b", 35.0)
        c = input_float("Число c", 24.0)
        print(f"-> Сумма двух наибольших = {task_2(a, b, c)}")
    elif choice == 3:
        xa, ya = input_float("Точка A: x", 0.0), input_float("Точка A: y", 0.0)
        xb, yb = input_float("Точка B: x", 3.0), input_float("Точка B: y", 4.0)
        xc, yc = input_float("Точка C: x", 1.0), input_float("Точка C: y", 1.0)
        pt, coords, d = task_3(xa, ya, xb, yb, xc, yc)
        print(f"-> Ближе точка {pt} с расстоянием {d:.4f}")
    elif choice == 4:
        x = input_float("Координата x (не 0)", -3.0)
        y = input_float("Координата y (не 0)", 5.0)
        print(f"-> Четверть № {task_4(x, y)}")
    elif choice == 5:
        n = input_int("Введите целое число", -8)
        print(f"-> Описание: «{task_5(n)}»")
    elif choice == 6:
        n = input_int("Число (1-999)", 42)
        print(f"-> Описание: «{task_6(n)}»")
    elif choice == 7:
        day = input_int("День (1-31)", 5)
        month = input_int("Месяц (1-12)", 1)
        print(f"-> Дата: «{task_7(day, month)}»")
    elif choice == 8:
        n = input_int("Количество заданий (10-40)", 18)
        print(f"-> Результат: «{task_8(n)}»")
    elif choice == 9:
        n = input_int("Число (100-999)", 256)
        print(f"-> Текст: «{task_9(n)}»")
    elif choice == 10:
        year = input_int("Номер года", 2026)
        print(f"-> По восточному календарю: «{task_10(year)}»")
    else:
        print("Неизвестный номер задачи.")

def main():
    print("=" * 60)
    print("Лабораторная работа №2: Алгоритмы ветвления")
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

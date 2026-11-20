def task_1(price_per_kg: float):
    """Задача 1: Стоимость 0.1, 0.2, ..., 1.0 кг конфет."""
    results = []
    for i in range(1, 11):
        weight = i / 10.0
        cost = weight * price_per_kg
        results.append((weight, round(cost, 2)))
    return results

def task_2(n: int):
    """Задача 2: Произведение 1.1 * 1.2 * ... (N сомножителей)."""
    product = 1.0
    for i in range(1, n + 1):
        factor = 1.0 + i * 0.1
        product *= factor
    return product

def task_3(n: int):
    """Задача 3: Квадрат N через сумму 1 + 3 + ... + (2*N - 1) с выводом промежуточных сумм."""
    current_sum = 0
    history = []
    for i in range(1, n + 1):
        odd = 2 * i - 1
        current_sum += odd
        history.append((odd, current_sum))
    return current_sum, history

def task_4(a: float, n: int):
    """Задача 4: Один цикл, сумма 1 + A + A^2 + ... + A^N."""
    total = 1.0
    current_power = 1.0
    for _ in range(n):
        current_power *= a
        total += current_power
    return total

def task_5(a: float, n: int):
    """Задача 5: Один цикл, 1 - A + A^2 - A^3 + ... +- A^N. Без условного оператора if."""
    total = 1.0
    term = 1.0
    # Знак меняется естественным образом путем умножения на (-a) без всяких if
    multiplier = -a
    for _ in range(n):
        term *= multiplier
        total += term
    return total

def task_6(a: int, b: int):
    """Задача 6: Числа от A до B, каждое выводится столько раз, каково его значение."""
    output = []
    for num in range(a, b + 1):
        for _ in range(num):
            output.append(num)
    return output

def task_7(a: float, b: float):
    """Задача 7: Остаток длины A после размещения отрезков длины B без умножения и деления."""
    remainder = a
    while remainder >= b:
        remainder -= b
    return remainder

def task_8(n: int):
    """Задача 8: Наименьшее K, для которого 1 + 2 + ... + K >= N, и сама сумма."""
    current_sum = 0
    k = 0
    while current_sum < n:
        k += 1
        current_sum += k
    return k, current_sum

def task_9(p: float):
    """Задача 9: Вклад 1000 руб. Увеличение на P% в месяц. Когда превысит 1100 руб."""
    deposit = 1000.0
    months = 0
    rate = p / 100.0
    while deposit <= 1100.0:
        months += 1
        deposit += deposit * rate
    return months, round(deposit, 2)

def task_10(a: int, b: int):
    """Задача 10: НОД алгоритмом Евклида."""
    x, y = a, b
    while y != 0:
        x, y = y, x % y
    return x

def main():
    print("=" * 60)
    print("Лабораторная работа №3: Циклические алгоритмы")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    # 1. Стоимость конфет
    print("Задание 1: Стоимость конфет (цена 450 руб/кг):")
    for w, c in task_1(450.0):
        print(f"  {w:.1f} кг = {c:.2f} руб.")

    # 2. Произведение сомножителей
    print(f"\nЗадание 2: N=5 => Произведение 1.1*1.2*...*1.5 = {task_2(5):.6f}")

    # 3. Квадрат числа
    sq, hist = task_3(5)
    print(f"\nЗадание 3: N=5 => N^2 = {sq}")
    for term, s in hist:
        print(f"  + {term} => текущая сумма = {s}")

    # 4. Сумма степеней
    print(f"\nЗадание 4: A=2, N=4 => 1 + 2 + 4 + 8 + 16 = {task_4(2.0, 4)}")

    # 5. Знакопеременная сумма (без if)
    print(f"Задание 5: A=2, N=4 => 1 - 2 + 4 - 8 + 16 = {task_5(2.0, 4)}")

    # 6. Повторение чисел
    seq = task_6(2, 4)
    print(f"Задание 6: A=2, B=4 => {seq}")

    # 7. Отрезки без умножения и деления
    rem = task_7(14.5, 3.0)
    print(f"Задание 7: A=14.5, B=3.0 => Незанятая длина = {rem:.2f}")

    # 8. Сумма 1+...+K >= N
    k8, sum8 = task_8(15)
    print(f"Задание 8: N=15 => K = {k8}, Сумма = {sum8}")

    # 9. Банковский вклад
    m9, s9 = task_9(3.5)
    print(f"Задание 9: P=3.5% => Месяцев = {m9}, Итоговая сумма = {s9} руб.")

    # 10. НОД алгоритмом Евклида
    nod10 = task_10(140, 96)
    print(f"Задание 10: НОД(140, 96) = {nod10}")
    print("=" * 60)

if __name__ == "__main__":
    main()

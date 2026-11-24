def input_int(prompt, default_val):
    try:
        val = input(f"{prompt} [по умолчанию {default_val}]: ").strip()
        return int(val) if val else int(default_val)
    except (ValueError, EOFError):
        return int(default_val)

# Задача 1: Спиральный обход нечетной квадратной матрицы против часовой стрелки
def task_1(matrix: list) -> list:
    m = len(matrix)
    res = []
    layers = (m + 1) // 2
    for l in range(layers):
        for r in range(l, m - l):
            res.append(matrix[r][l])
        for c in range(l + 1, m - l):
            res.append(matrix[m - 1 - l][c])
        for r in range(m - 2 - l, l - 1, -1):
            res.append(matrix[r][m - 1 - l])
        for c in range(m - 2 - l, l, -1):
            res.append(matrix[l][c])
    return res

# Задача 2: Сумма и произведение элементов K-й строки (1-based)
def task_2(matrix: list, k: int):
    row = matrix[k - 1]
    p = 1
    for x in row:
        p *= x
    return sum(row), p

# Задача 3: Номер столбца с наименьшим произведением и само произведение
def task_3(matrix: list):
    m = len(matrix)
    n = len(matrix[0])
    min_col = 1
    min_prod = float('inf')
    for c in range(n):
        prod = 1
        for r in range(m):
            prod *= matrix[r][c]
        if c == 0 or prod < min_prod:
            min_prod = prod
            min_col = c + 1
    return min_col, min_prod

# Задача 4: Количество элементов больше среднего в каждом столбце
def task_4(matrix: list) -> list:
    m, n = len(matrix), len(matrix[0])
    counts = []
    for c in range(n):
        col_vals = [matrix[r][c] for r in range(m)]
        avg = sum(col_vals) / m
        counts.append(sum(1 for v in col_vals if v > avg))
    return counts

# Задача 5: Номер первого столбца только из нечетных чисел
def task_5(matrix: list) -> int:
    m, n = len(matrix), len(matrix[0])
    for c in range(n):
        if all(matrix[r][c] % 2 != 0 for r in range(m)):
            return c + 1
    return 0

# Задача 6: Обмен min и max в каждой строке
def task_6(matrix: list) -> list:
    res = [row[:] for row in matrix]
    for row in res:
        i_min = row.index(min(row))
        i_max = row.index(max(row))
        row[i_min], row[i_max] = row[i_max], row[i_min]
    return res

# Задача 7: Обмен столбцов с глобальным min и max
def task_7(matrix: list) -> list:
    m, n = len(matrix), len(matrix[0])
    mn, mx = float('inf'), float('-inf')
    c_mn, c_mx = 0, 0
    for r in range(m):
        for c in range(n):
            if matrix[r][c] < mn:
                mn, c_mn = matrix[r][c], c
            if matrix[r][c] > mx:
                mx, c_mx = matrix[r][c], c
    res = [row[:] for row in matrix]
    for r in range(m):
        res[r][c_mn], res[r][c_mx] = res[r][c_mx], res[r][c_mn]
    return res

# Задача 8: Обмен левой верхней и правой нижней четвертей
def task_8(matrix: list) -> list:
    m, n = len(matrix), len(matrix[0])
    hm, hn = m // 2, n // 2
    res = [row[:] for row in matrix]
    for r in range(hm):
        for c in range(hn):
            res[r][c], res[r + hm][c + hn] = res[r + hm][c + hn], res[r][c]
    return res

# Задача 9: Сортировка строк по возрастанию первого элемента
def task_9(matrix: list) -> list:
    return sorted(matrix, key=lambda row: row[0])

# Задача 10: Суммы диагоналей, параллельных главной
def task_10(matrix: list) -> list:
    m = len(matrix)
    diagonals = []
    for d in range(m - 1, -m, -1):
        s = 0
        elems = []
        for r in range(m):
            c = r - d
            if 0 <= c < m:
                s += matrix[r][c]
                elems.append(matrix[r][c])
        diagonals.append((elems, s))
    return diagonals

def run_all_demo():
    print("\n--- Демонстрационный запуск всех заданий ---")
    m3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(f"Задание 1 (спираль 3x3): {task_1(m3)}")
    m4 = [[1, 2, 3, 4], [5, 1, 2, 3], [4, 2, 5, 1]]
    s2, p2 = task_2(m4, 2)
    print(f"Задание 2 (строка 2): Сумма={s2}, Произведение={p2}")
    c3, pr3 = task_3(m4)
    print(f"Задание 3: Мин. произведение в столбце №{c3} = {pr3}")
    print(f"Задание 4: Элементов больше среднего по столбцам: {task_4(m4)}")
    m5 = [[2, 3, 4], [4, 7, 6], [8, 5, 2]]
    print(f"Задание 5: Первый нечетный столбец №: {task_5(m5)}")
    m6 = [[9, 2, 5], [1, 8, 3]]
    print(f"Задание 6 (обмен min/max в строках): {task_6(m6)}")
    m7 = [[10, 20, 5], [99, 15, 30]]
    print(f"Задание 7 (обмен столбцов глобального min и max): {task_7(m7)}")
    m8 = [[1, 2, 7, 8], [3, 4, 9, 1], [5, 5, 99, 99], [6, 6, 88, 88]]
    print(f"Задание 8 (обмен четвертей):\n  {task_8(m8)[0]}\n  {task_8(m8)[1]}\n  {task_8(m8)[2]}\n  {task_8(m8)[3]}")
    m9 = [[50, 1, 2], [10, 8, 9], [30, 4, 5]]
    print(f"Задание 9 (сортировка строк): {task_9(m9)}")
    print("Задание 10 (суммы диагоналей):")
    for el, sm in task_10(m3):
        print(f"  {el} -> сумма = {sm}")

def run_interactive():
    print("\nДоступные номера задач: 1 - 10")
    try:
        choice = int(input("Введите номер задачи для проверки (1-10): ").strip())
    except (ValueError, EOFError):
        choice = 1

    m_demo = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    if choice == 1:
        print(f"Исходная матрица:\n {m_demo[0]}\n {m_demo[1]}\n {m_demo[2]}")
        print(f"-> Спиральный обход: {task_1(m_demo)}")
    elif choice == 2:
        k = input_int("Номер строки K (1-3)", 2)
        s, p = task_2(m_demo, k)
        print(f"-> Строка {k}: Сумма = {s}, Произведение = {p}")
    elif choice == 3:
        col, prod = task_3(m_demo)
        print(f"-> Столбец № {col} с минимальным произведением = {prod}")
    elif choice == 4:
        print(f"-> Количество элементов > среднего: {task_4(m_demo)}")
    elif choice == 5:
        m5 = [[2, 3, 4], [4, 7, 6], [8, 5, 2]]
        print(f"Матрица:\n {m5[0]}\n {m5[1]}\n {m5[2]}")
        print(f"-> Номер первого чисто нечетного столбца: {task_5(m5)}")
    elif choice == 6:
        m6 = [[9, 2, 5], [1, 8, 3]]
        print(f"До: {m6}\n-> После замены min и max: {task_6(m6)}")
    elif choice == 7:
        m7 = [[10, 20, 5], [99, 15, 30]]
        print(f"До: {m7}\n-> После обмена столбцов min и max: {task_7(m7)}")
    elif choice == 8:
        m8 = [[1, 2, 7, 8], [3, 4, 9, 1], [5, 5, 99, 99], [6, 6, 88, 88]]
        print(f"-> Четверти обменены:\n {task_8(m8)}")
    elif choice == 9:
        m9 = [[50, 1, 2], [10, 8, 9], [30, 4, 5]]
        print(f"-> Строки упорядочены:\n {task_9(m9)}")
    elif choice == 10:
        print(f"-> Диагонали матрицы 3х3:")
        for el, sm in task_10(m_demo):
            print(f"   {el} -> {sm}")
    else:
        print("Неизвестный номер задачи.")

def main():
    print("=" * 60)
    print("Лабораторная работа №6: Двумерные массивы")
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

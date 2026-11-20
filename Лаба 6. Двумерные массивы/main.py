def task_1(matrix: list) -> list:
    """Задача 1: Обход квадратной матрицы нечетного порядка против часовой стрелки по спирали."""
    m = len(matrix)
    result = []
    layers = (m + 1) // 2
    for l in range(layers):
        # 1. Первый (левый) столбец сверху вниз
        for r in range(l, m - l):
            result.append(matrix[r][l])
        # 2. Последняя (нижняя) строка слева направо
        for c in range(l + 1, m - l):
            result.append(matrix[m - 1 - l][c])
        # 3. Последний (правый) столбец снизу вверх
        for r in range(m - 2 - l, l - 1, -1):
            result.append(matrix[r][m - 1 - l])
        # 4. Первая (верхняя) строка справа налево
        for c in range(m - 2 - l, l, -1):
            result.append(matrix[l][c])
    return result

def task_2(matrix: list, k: int):
    """Задача 2: Сумма и произведение элементов K-й строки (1-based)."""
    row = matrix[k - 1]
    row_sum = sum(row)
    row_prod = 1
    for x in row:
        row_prod *= x
    return row_sum, row_prod

def task_3(matrix: list):
    """Задача 3: Номер столбца (1-based) с наименьшим произведением и само произведение."""
    m = len(matrix)
    n = len(matrix[0])
    min_col_idx = 1
    min_prod = float('inf')
    
    for c in range(n):
        col_prod = 1
        for r in range(m):
            col_prod *= matrix[r][c]
        if c == 0 or col_prod < min_prod:
            min_prod = col_prod
            min_col_idx = c + 1
    return min_col_idx, min_prod

def task_4(matrix: list) -> list:
    """Задача 4: В каждом столбце количество элементов, больших среднего арифметического этого столбца."""
    m = len(matrix)
    n = len(matrix[0])
    counts = []
    for c in range(n):
        col_vals = [matrix[r][c] for r in range(m)]
        avg = sum(col_vals) / m
        cnt = sum(1 for v in col_vals if v > avg)
        counts.append(cnt)
    return counts

def task_5(matrix: list) -> int:
    """Задача 5: Номер первого столбца (1-based), содержащего только нечетные числа (или 0)."""
    m = len(matrix)
    n = len(matrix[0])
    for c in range(n):
        if all(matrix[r][c] % 2 != 0 for r in range(m)):
            return c + 1
    return 0

def task_6(matrix: list) -> list:
    """Задача 6: Поменять местами минимальный и максимальный элемент в каждой строке."""
    # Возвращаем копию матрицы с переставленными элементами
    res = [row[:] for row in matrix]
    for row in res:
        min_idx = row.index(min(row))
        max_idx = row.index(max(row))
        row[min_idx], row[max_idx] = row[max_idx], row[min_idx]
    return res

def task_7(matrix: list) -> list:
    """Задача 7: Поменять местами столбцы, содержащие минимальный и максимальный элементы матрицы."""
    m = len(matrix)
    n = len(matrix[0])
    min_val = float('inf')
    max_val = float('-inf')
    min_col = 0
    max_col = 0
    
    for r in range(m):
        for c in range(n):
            val = matrix[r][c]
            if val < min_val:
                min_val = val
                min_col = c
            if val > max_val:
                max_val = val
                max_col = c
                
    res = [row[:] for row in matrix]
    for r in range(m):
        res[r][min_col], res[r][max_col] = res[r][max_col], res[r][min_col]
    return res

def task_8(matrix: list) -> list:
    """Задача 8: Поменять местами левую верхнюю и правую нижнюю четверти матрицы (M и N четные)."""
    m = len(matrix)
    n = len(matrix[0])
    half_m = m // 2
    half_n = n // 2
    res = [row[:] for row in matrix]
    for r in range(half_m):
        for c in range(half_n):
            res[r][c], res[r + half_m][c + half_n] = res[r + half_m][c + half_n], res[r][c]
    return res

def task_9(matrix: list) -> list:
    """Задача 9: Упорядочить строки матрицы по возрастанию первых элементов."""
    return sorted(matrix, key=lambda row: row[0])

def task_10(matrix: list) -> list:
    """Задача 10: Суммы элементов каждой диагонали, параллельной главной, начиная с одноэлементной."""
    m = len(matrix)
    # Диагонали, параллельные главной: элементы с постоянной разностью (col - row) или (row - col)
    # Начиная с одноэлементной: сначала под главной (снизу вверх) или над главной (сверху вниз).
    # Всего 2*m - 1 диагоналей:
    # d от -(m-1) до m-1: row - col = d
    # d = m-1: A[m-1][0] (1 элемент)
    # ...
    # d = 0: главная диагональ (m элементов)
    # ...
    # d = -(m-1): A[0][m-1] (1 элемент)
    diagonals = []
    # Начинаем с одноэлементной в левом нижнем углу:
    for d in range(m - 1, -m, -1):
        s = 0
        diag_elems = []
        for r in range(m):
            c = r - d
            if 0 <= c < m:
                s += matrix[r][c]
                diag_elems.append(matrix[r][c])
        diagonals.append((diag_elems, s))
    return diagonals

def main():
    print("=" * 60)
    print("Лабораторная работа №6: Двумерные массивы")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    # 1. Спираль против часовой стрелки
    mat3 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print(f"Задание 1: Исходная 3x3:\n {mat3[0]}\n {mat3[1]}\n {mat3[2]}")
    print(f"Спираль против часовой: {task_1(mat3)}")

    # 2. Сумма и произведение K-й строки
    mat4 = [
        [1, 2, 3, 4],
        [5, 1, 2, 3],
        [4, 2, 5, 1]
    ]
    s2, p2 = task_2(mat4, 2)
    print(f"\nЗадание 2: Строка 2 {mat4[1]} => Сумма={s2}, Произведение={p2}")

    # 3. Столбец с наименьшим произведением
    col3, prod3 = task_3(mat4)
    print(f"\nЗадание 3: Столбец с мин. произведением = №{col3} со значением {prod3}")

    # 4. Элементов больше среднего в каждом столбце
    print(f"\nЗадание 4: В каждом столбце кол-во элементов > среднего: {task_4(mat4)}")

    # 5. Первый столбец из нечетных чисел
    mat5 = [
        [2, 3, 4],
        [4, 7, 6],
        [8, 5, 2]
    ]
    print(f"\nЗадание 5: Матрица:\n {mat5[0]}\n {mat5[1]}\n {mat5[2]}")
    print(f"Номер первого чисто нечетного столбца: {task_5(mat5)}")

    # 6. Замена min и max в строках
    mat6 = [
        [9, 2, 5],
        [1, 8, 3]
    ]
    print(f"\nЗадание 6: До:\n {mat6[0]}\n {mat6[1]}")
    after6 = task_6(mat6)
    print(f"После замены min и max в строках:\n {after6[0]}\n {after6[1]}")

    # 7. Замена столбцов min и max матрицы
    mat7 = [
        [10, 20, 5],
        [99, 15, 30]
    ]
    print(f"\nЗадание 7: Столбцы с мин (5 в ст.3) и макс (99 в ст.1) меняются:")
    after7 = task_7(mat7)
    for row in after7:
        print(" ", row)

    # 8. Четверти матрицы
    mat8 = [
        [1, 2,  7, 8],
        [3, 4,  9, 1],
        [5, 5, 99, 99],
        [6, 6, 88, 88]
    ]
    print(f"\nЗадание 8: Перестановка левой верхней и правой нижней четвертей:")
    after8 = task_8(mat8)
    for row in after8:
        print(" ", row)

    # 9. Сортировка строк по первому элементу
    mat9 = [
        [50, 1, 2],
        [10, 8, 9],
        [30, 4, 5]
    ]
    print(f"\nЗадание 9: Упорядочивание строк по 1-му элементу:")
    for row in task_9(mat9):
        print(" ", row)

    # 10. Диагонали, параллельные главной
    print(f"\nЗадание 10: Суммы диагоналей, параллельных главной (3x3):")
    for elems, total in task_10(mat3):
        print(f"  Элементы {elems} => сумма = {total}")
    print("=" * 60)

if __name__ == "__main__":
    main()

def input_list_int(prompt, default_str):
    try:
        val = input(f"{prompt} [по умолчанию {default_str}]: ").strip()
        s = val if val else default_str
        return [int(x) for x in s.split()]
    except (ValueError, EOFError):
        return [int(x) for x in default_str.split()]

# Алгоритм сортировки выбором
def selection_sort(arr: list, trace: bool = False):
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0

    if trace:
        print(f"Исходный массив: {a}")

    for i in range(n - 1):
        min_idx = i
        if trace:
            print(f"\n--- Шаг {i + 1}: поиск минимума в суффиксе [{i}..{n-1}] ---")

        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j

        if trace:
            print(f"  Найден минимум: {a[min_idx]} на индексе {min_idx}")

        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
            if trace:
                print(f"  Обмен a[{i}] и a[{min_idx}] => {a}")
        else:
            if trace:
                print(f"  Элемент {a[i]} уже на своей позиции {i}")

    return a, comparisons, swaps

def run_all_demo():
    demo_arr = [64, 25, 12, 22, 11]
    print("\n1. Пошаговая трассировка алгоритма:")
    sorted_demo, cmp_cnt, swp_cnt = selection_sort(demo_arr, trace=True)
    print(f"\nРезультат: {sorted_demo}")
    print(f"Сравнений: {cmp_cnt}, Обменов: {swp_cnt}")

    test_cases = {
        "Случайный массив": [29, 10, 14, 37, 13],
        "Уже отсортированный массив": [1, 2, 3, 4, 5],
        "Массив в обратном порядке": [5, 4, 3, 2, 1],
        "Массив с дубликатами": [3, 1, 4, 1, 5, 9, 2]
    }
    print("\n2. Анализ эффективности на разных наборах данных:")
    print(f"{'Тип набора данных':<35} | {'Длина':<6} | {'Сравнений':<10} | {'Обменов':<10}")
    print("-" * 70)
    for name, test_arr in test_cases.items():
        _, c, s = selection_sort(test_arr, trace=False)
        print(f"{name:<35} | {len(test_arr):<6} | {c:<10} | {s:<10}")

def run_interactive():
    print("\nВведите свой массив чисел через пробел для сортировки выбором.")
    arr = input_list_int("Массив", "50 20 80 10 40 30")
    sorted_arr, c, s = selection_sort(arr, trace=True)
    print(f"\n-> Итог: {sorted_arr}")
    print(f"-> Сравнений: {c}, обменов: {s}")

def main():
    print("=" * 60)
    print("Лабораторная работа №9: Сортировка выбором")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    print("\nВыберите режим работы:")
    print("1 - Запустить демонстрацию со стандартными тестами")
    print("2 - Ввести свой массив чисел для пошаговой сортировки")
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

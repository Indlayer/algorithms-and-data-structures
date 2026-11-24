def input_list_int(prompt, default_str):
    try:
        val = input(f"{prompt} [по умолчанию {default_str}]: ").strip()
        s = val if val else default_str
        return [int(x) for x in s.split()]
    except (ValueError, EOFError):
        return [int(x) for x in default_str.split()]

# Алгоритм сортировки пузырьком с оптимизацией
def bubble_sort(arr: list, trace: bool = False):
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0

    if trace:
        print(f"Исходный массив: {a}")

    for i in range(n - 1):
        swapped = False
        if trace:
            print(f"\n--- Проход {i + 1} ---")
        for j in range(n - 1 - i):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
                if trace:
                    print(f"  Обмен a[{j}]={a[j+1]} и a[{j+1}]={a[j]} => {a}")
            else:
                if trace:
                    print(f"  Без обмена ({a[j]} <= {a[j+1]})")
        if not swapped:
            if trace:
                print("  Массив уже упорядочен (досрочный выход благодаря флагу swapped).")
            break

    return a, comparisons, swaps

def run_all_demo():
    demo_list = [64, 34, 25, 12, 22, 11, 90]
    print("\n1. Пошаговая трассировка алгоритма:")
    sorted_demo, cmp_cnt, swp_cnt = bubble_sort(demo_list, trace=True)
    print(f"\nРезультат: {sorted_demo}")
    print(f"Сравнений: {cmp_cnt}, Перестановок: {swp_cnt}")

    test_cases = {
        "Случайный массив": [29, 10, 14, 37, 13],
        "Уже отсортированный массив (лучший случай)": [1, 2, 3, 4, 5],
        "Массив в обратном порядке (худший случай)": [5, 4, 3, 2, 1],
        "Массив с дубликатами": [5, 2, 8, 5, 2, 8, 1]
    }
    print("\n2. Анализ эффективности на разных наборах данных:")
    print(f"{'Тип набора данных':<45} | {'Сравнений':<10} | {'Перестановок':<12}")
    print("-" * 75)
    for name, test_arr in test_cases.items():
        _, c, s = bubble_sort(test_arr, trace=False)
        print(f"{name:<45} | {c:<10} | {s:<12}")

def run_interactive():
    print("\nВведите свой массив чисел через пробел для сортировки пузырьком.")
    arr = input_list_int("Массив", "45 12 89 23 7 60 11")
    sorted_arr, c, s = bubble_sort(arr, trace=True)
    print(f"\n-> Итог: {sorted_arr}")
    print(f"-> Всего сравнений: {c}, перестановок: {s}")

def main():
    print("=" * 60)
    print("Лабораторная работа №7: Сортировка пузырьком")
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

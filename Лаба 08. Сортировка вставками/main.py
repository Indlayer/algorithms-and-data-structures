def input_list_int(prompt, default_str):
    try:
        val = input(f"{prompt} [по умолчанию {default_str}]: ").strip()
        s = val if val else default_str
        return [int(x) for x in s.split()]
    except (ValueError, EOFError):
        return [int(x) for x in default_str.split()]

# Алгоритм сортировки вставками
def insertion_sort(arr: list, trace: bool = False):
    a = arr.copy()
    n = len(a)
    comparisons = 0
    shifts = 0

    if trace:
        print(f"Исходный массив: {a}")

    for i in range(1, n):
        key = a[i]
        j = i - 1
        if trace:
            print(f"\n--- Шаг {i}: вставка ключа key={key} ---")

        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                if trace:
                    print(f"  Сдвиг a[{j}]={a[j]} вправо")
                j -= 1
            else:
                break

        a[j + 1] = key
        if trace:
            print(f"  Вставка key={key} на позицию {j + 1} => {a}")

    return a, comparisons, shifts

def run_all_demo():
    demo_arr = [12, 11, 13, 5, 6, 7]
    print("\n1. Пошаговая трассировка алгоритма:")
    sorted_demo, cmp_cnt, shf_cnt = insertion_sort(demo_arr, trace=True)
    print(f"\nРезультат: {sorted_demo}")
    print(f"Сравнений: {cmp_cnt}, Сдвигов: {shf_cnt}")

    test_cases = {
        "Случайный массив": [31, 41, 59, 26, 41, 58],
        "Уже отсортированный массив (лучший случай)": [1, 2, 3, 4, 5, 6],
        "Массив в обратном порядке (худший случай)": [6, 5, 4, 3, 2, 1],
        "Массив с дубликатами": [4, 2, 4, 2, 4, 1]
    }
    print("\n2. Анализ эффективности на разных наборах данных:")
    print(f"{'Тип набора данных':<45} | {'Сравнений':<10} | {'Сдвигов':<10}")
    print("-" * 75)
    for name, test_arr in test_cases.items():
        _, c, s = insertion_sort(test_arr, trace=False)
        print(f"{name:<45} | {c:<10} | {s:<10}")

def run_interactive():
    print("\nВведите свой массив чисел через пробел для сортировки вставками.")
    arr = input_list_int("Массив", "34 10 64 51 32 21")
    sorted_arr, c, s = insertion_sort(arr, trace=True)
    print(f"\n-> Итог: {sorted_arr}")
    print(f"-> Сравнений: {c}, сдвигов: {s}")

def main():
    print("=" * 60)
    print("Лабораторная работа №8: Сортировка вставками")
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

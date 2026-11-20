def bubble_sort(arr: list, trace: bool = False):
    """
    Классическая сортировка пузырьком с оптимизацией (флаг обменов).
    Возвращает отсортированный массив, количество сравнений и количество перестановок.
    """
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
                    print(f"  Обмен элементов a[{j}]={a[j+1]} и a[{j+1}]={a[j]} => {a}")
            else:
                if trace:
                    print(f"  Без обмена (a[{j}]={a[j]} <= a[{j+1}]={a[j+1]})")
        if not swapped:
            if trace:
                print("  Массив уже упорядочен (досрочный выход благодаря оптимизации).")
            break
            
    return a, comparisons, swaps

def main():
    print("=" * 60)
    print("Лабораторная работа №7: Сортировка пузырьком")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    # 1. Демонстрация с подробным пошаговым выводом
    demo_list = [64, 34, 25, 12, 22, 11, 90]
    print("1. Пошаговая трассировка алгоритма:")
    sorted_demo, cmp_cnt, swp_cnt = bubble_sort(demo_list, trace=True)
    print(f"\nРезультат: {sorted_demo}")
    print(f"Сравнений: {cmp_cnt}, Перестановок: {swp_cnt}")

    # 2. Тестирование различных сценариев
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

    print("=" * 60)

if __name__ == "__main__":
    main()

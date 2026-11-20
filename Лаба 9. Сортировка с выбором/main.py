def selection_sort(arr: list, trace: bool = False):
    """
    Классическая сортировка выбором (Selection Sort).
    На каждом шаге ищется минимальный элемент в оставшейся части массива и меняется с текущим.
    Возвращает отсортированный массив, количество сравнений и количество обменов.
    """
    a = arr.copy()
    n = len(a)
    comparisons = 0
    swaps = 0
    
    if trace:
        print(f"Исходный массив: {a}")
        
    for i in range(n - 1):
        min_idx = i
        if trace:
            print(f"\n--- Шаг {i + 1}: поиск минимума в диапазоне индексов [{i}..{n-1}] ---")
            
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
                
        if trace:
            print(f"  Найден минимум: {a[min_idx]} на позиции {min_idx}")
            
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
            if trace:
                print(f"  Обмен элементов на позициях {i} и {min_idx} => {a}")
        else:
            if trace:
                print(f"  Элемент {a[i]} уже стоит на своей правильной позиции {i}")
                
    return a, comparisons, swaps

def main():
    print("=" * 60)
    print("Лабораторная работа №9: Сортировка выбором")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    # 1. Пошаговая трассировка
    demo_arr = [64, 25, 12, 22, 11]
    print("1. Пошаговая трассировка алгоритма:")
    sorted_demo, cmp_cnt, swp_cnt = selection_sort(demo_arr, trace=True)
    print(f"\nРезультат: {sorted_demo}")
    print(f"Сравнений: {cmp_cnt}, Обменов: {swp_cnt}")

    # 2. Анализ на различных наборах данных
    test_cases = {
        "Случайный массив": [29, 10, 14, 37, 13],
        "Уже отсортированный массив": [1, 2, 3, 4, 5],
        "Массив в обратном порядке": [5, 4, 3, 2, 1],
        "Массив с дубликатами": [3, 1, 4, 1, 5, 9, 2, 6, 5]
    }

    print("\n2. Анализ эффективности на разных наборах данных:")
    print(f"{'Тип набора данных':<40} | {'Длина':<6} | {'Сравнений':<10} | {'Обменов':<10}")
    print("-" * 75)
    for name, test_arr in test_cases.items():
        _, c, s = selection_sort(test_arr, trace=False)
        print(f"{name:<40} | {len(test_arr):<6} | {c:<10} | {s:<10}")

    print("=" * 60)

if __name__ == "__main__":
    main()

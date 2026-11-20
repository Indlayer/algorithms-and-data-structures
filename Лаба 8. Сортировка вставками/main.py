def insertion_sort(arr: list, trace: bool = False):
    """
    Классическая сортировка вставками (Insertion Sort).
    Возвращает отсортированный массив, количество сравнений и сдвигов.
    """
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
            print(f"\n--- Шаг {i}: вставляем ключ key={key} из позиции {i} ---")
            
        # Сдвигаем элементы a[0..i-1], которые больше key, на одну позицию вправо
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                if trace:
                    print(f"  Сдвиг a[{j}]={a[j]} на позицию {j+1}")
                j -= 1
            else:
                break
                
        a[j + 1] = key
        if trace:
            print(f"  Вставка ключа {key} на позицию {j + 1} => {a}")
            
    return a, comparisons, shifts

def main():
    print("=" * 60)
    print("Лабораторная работа №8: Сортировка вставками")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    # 1. Пошаговая трассировка
    demo_arr = [12, 11, 13, 5, 6, 7]
    print("1. Пошаговая трассировка алгоритма:")
    sorted_demo, cmp_cnt, shf_cnt = insertion_sort(demo_arr, trace=True)
    print(f"\nРезультат: {sorted_demo}")
    print(f"Сравнений: {cmp_cnt}, Сдвигов: {shf_cnt}")

    # 2. Анализ на различных наборах данных
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

    print("=" * 60)

if __name__ == "__main__":
    main()

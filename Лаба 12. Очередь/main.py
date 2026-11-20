class Queue:
    """
    Класс реализации структуры данных 'Очередь' (FIFO - First In, First Out).
    """
    def __init__(self, max_size: int = None):
        self._items = []
        self._max_size = max_size

    def is_empty(self) -> bool:
        """Проверка очереди на пустоту."""
        return len(self._items) == 0

    def is_full(self) -> bool:
        """Проверка на заполненность (если задан max_size)."""
        if self._max_size is None:
            return False
        return len(self._items) >= self._max_size

    def enqueue(self, item):
        """Добавление элемента в конец очереди."""
        if self.is_full():
            raise OverflowError(f"Переполнение очереди! Максимальная вместимость: {self._max_size}")
        self._items.append(item)

    def dequeue(self):
        """Извлечение и возврат первого элемента из начала очереди."""
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустой очереди!")
        return self._items.pop(0)

    def peek(self):
        """Просмотр первого элемента без его извлечения."""
        if self.is_empty():
            raise IndexError("Очередь пуста!")
        return self._items[0]

    def size(self) -> int:
        """Количество элементов в очереди."""
        return len(self._items)

    def clear(self):
        """Очистить очередь."""
        self._items.clear()

    def __str__(self):
        if self.is_empty():
            return "Queue([]) (пусто)"
        return " -> ".join(map(str, self._items)) + " (конец очереди)"


class WebTaskDispatcher:
    """
    Прикладной пример использования очереди: диспетчер задач веб-сервера.
    Запросы пользователей ставятся в очередь и обрабатываются строго по принципу FIFO.
    """
    def __init__(self):
        self.queue = Queue(max_size=10)

    def add_request(self, request_id: int, client: str, action: str):
        task = {"id": request_id, "client": client, "action": action}
        print(f"  [+] Поступил HTTP-запрос #{request_id} от '{client}': {action}")
        self.queue.enqueue(task)

    def process_next_request(self):
        if self.queue.is_empty():
            print("  [-] Все запросы обработаны. Очередь пуста.")
            return
        task = self.queue.dequeue()
        print(f"  [*] Обработан запрос #{task['id']} от '{task['client']}': {task['action']} (осталось в очереди: {self.queue.size()})")


def main():
    print("=" * 60)
    print("Лабораторная работа №12: Очередь (FIFO)")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    # 1. Базовые операции с очередью
    print("1. Тестирование базовых операций класса Queue:")
    q = Queue(max_size=5)
    print(f"Очередь пуста? {q.is_empty()}")

    for num in [10, 20, 30]:
        q.enqueue(num)
        print(f"  Добавлено {num} => Текущее состояние: {q}")

    print(f"Размер очереди: {q.size()}")
    print(f"Первый элемент (peek): {q.peek()}")

    extracted = q.dequeue()
    print(f"Извлечен элемент (dequeue): {extracted}")
    print(f"Состояние после извлечения: {q}")

    # 2. Обработка исключений
    print("\n2. Обработка граничных ситуаций:")
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    print(f"Очередь заполнена: {q} (размер: {q.size()})")
    try:
        q.enqueue(70)
    except OverflowError as e:
        print(f"  [Исключение] {e}")

    # 3. Прикладной сценарий: Диспетчер веб-запросов
    print("\n3. Прикладной сценарий: Имитация обработки запросов веб-сервера:")
    dispatcher = WebTaskDispatcher()
    dispatcher.add_request(101, "Пользователь_A", "GET /api/profile")
    dispatcher.add_request(102, "Пользователь_B", "POST /api/order/create")
    dispatcher.add_request(103, "Пользователь_C", "GET /catalog")

    print("\nОбработка запросов сервером (FIFO):")
    while not dispatcher.queue.is_empty():
        dispatcher.process_next_request()

    print("=" * 60)

if __name__ == "__main__":
    main()

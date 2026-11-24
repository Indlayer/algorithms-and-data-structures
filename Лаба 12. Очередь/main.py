def input_int(prompt, default_val):
    try:
        val = input(f"{prompt} [по умолчанию {default_val}]: ").strip()
        return int(val) if val else int(default_val)
    except (ValueError, EOFError):
        return int(default_val)

def input_str(prompt, default_val):
    try:
        val = input(f"{prompt} [по умолчанию '{default_val}']: ").strip()
        return val if val else default_val
    except (ValueError, EOFError):
        return default_val

# Класс Очередь (FIFO - First In, First Out)
class Queue:
    def __init__(self, max_size: int = None):
        self._items = []
        self._max_size = max_size

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def is_full(self) -> bool:
        if self._max_size is None:
            return False
        return len(self._items) >= self._max_size

    def enqueue(self, item):
        if self.is_full():
            raise OverflowError(f"Переполнение очереди (максимум {self._max_size})")
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Попытка извлечения из пустой очереди")
        return self._items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("Очередь пуста")
        return self._items[0]

    def size(self) -> int:
        return len(self._items)

    def clear(self):
        self._items.clear()

    def __str__(self):
        if self.is_empty():
            return "Очередь пуста"
        return " -> ".join(map(str, self._items)) + " (хвост)"

# Диспетчер задач веб-сервера
class WebTaskDispatcher:
    def __init__(self):
        self.queue = Queue(max_size=10)

    def add_request(self, req_id: int, client: str, action: str):
        task = {"id": req_id, "client": client, "action": action}
        print(f"  [+] Запрос #{req_id} от '{client}': {action}")
        self.queue.enqueue(task)

    def process_next_request(self):
        if self.queue.is_empty():
            print("  [-] Все запросы обработаны. Очередь пуста.")
            return
        task = self.queue.dequeue()
        print(f"  [*] Обработан запрос #{task['id']} от '{task['client']}': {task['action']} (в очереди: {self.queue.size()})")

def run_all_demo():
    print("\n1. Тестирование базовых операций очереди:")
    q = Queue(max_size=5)
    print(f"Очередь пуста? {q.is_empty()}")
    for num in [10, 20, 30]:
        q.enqueue(num)
        print(f"  Добавлено {num} => Состояние: {q}")
    print(f"Размер: {q.size()}, первый элемент (peek): {q.peek()}")
    print(f"Извлечен (dequeue): {q.dequeue()}")
    print(f"Состояние: {q}")

    print("\n2. Моделирование обработки запросов веб-сервера (FIFO):")
    dispatcher = WebTaskDispatcher()
    dispatcher.add_request(101, "Пользователь_A", "GET /api/profile")
    dispatcher.add_request(102, "Пользователь_B", "POST /api/order/create")
    dispatcher.add_request(103, "Пользователь_C", "GET /catalog")
    print("\nОбработка сервером в порядке поступления:")
    while not dispatcher.queue.is_empty():
        dispatcher.process_next_request()

def run_interactive():
    print("\nИнтерактивное управление очередью:")
    max_cap = input_int("Максимальная вместимость очереди", 5)
    q = Queue(max_size=max_cap)
    
    print("\nКоманды:")
    print("1 - Добавить элемент (enqueue)")
    print("2 - Извлечь первый элемент (dequeue)")
    print("3 - Посмотреть первый элемент (peek)")
    print("4 - Показать состояние очереди")
    print("0 - Выход в главное меню")

    while True:
        try:
            cmd = input("\nВыберите действие (0-4): ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if cmd == "1":
            item = input_str("Введите значение элемента", "Запрос-1")
            try:
                q.enqueue(item)
                print(f"-> Добавлено: {item}. Текущая очередь: {q}")
            except OverflowError as e:
                print(f"-> Ошибка: {e}")
        elif cmd == "2":
            try:
                val = q.dequeue()
                print(f"-> Извлечен элемент: {val}. Осталось в очереди: {q}")
            except IndexError as e:
                print(f"-> Ошибка: {e}")
        elif cmd == "3":
            try:
                print(f"-> Первый элемент в очереди: {q.peek()}")
            except IndexError as e:
                print(f"-> Ошибка: {e}")
        elif cmd == "4":
            print(f"-> Очередь ({q.size()} из {max_cap}): {q}")
        elif cmd == "0" or not cmd:
            break
        else:
            print("Неизвестная команда.")

def main():
    print("=" * 60)
    print("Лабораторная работа №12: Очередь (FIFO)")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    print("\nВыберите режим работы:")
    print("1 - Запустить авто-демонстрацию работы очереди")
    print("2 - Интерактивное управление очередью (enqueue/dequeue)")
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

from collections import deque

def input_list_int(prompt, default_str):
    try:
        val = input(f"{prompt} [по умолчанию {default_str}]: ").strip()
        s = val if val else default_str
        return [int(x) for x in s.split()]
    except (ValueError, EOFError):
        return [int(x) for x in default_str.split()]

def input_int(prompt, default_val):
    try:
        val = input(f"{prompt} [по умолчанию {default_val}]: ").strip()
        return int(val) if val else int(default_val)
    except (ValueError, EOFError):
        return int(default_val)

# Узел бинарного дерева
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Двоичное дерево поиска (BST)
class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self._insert_rec(self.root, value)

    def _insert_rec(self, node: TreeNode, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_rec(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_rec(node.right, value)

    def search(self, value) -> bool:
        curr = self.root
        while curr:
            if curr.value == value:
                return True
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return False

    # Прямой обход (Pre-order): Корень -> Левый -> Правый
    def pre_order(self) -> list:
        res = []
        def _walk(n):
            if n:
                res.append(n.value)
                _walk(n.left)
                _walk(n.right)
        _walk(self.root)
        return res

    # Симметричный обход (In-order): Левый -> Корень -> Правый (дает отсортированный список)
    def in_order(self) -> list:
        res = []
        def _walk(n):
            if n:
                _walk(n.left)
                res.append(n.value)
                _walk(n.right)
        _walk(self.root)
        return res

    # Обратный обход (Post-order): Левый -> Правый -> Корень
    def post_order(self) -> list:
        res = []
        def _walk(n):
            if n:
                _walk(n.left)
                _walk(n.right)
                res.append(n.value)
        _walk(self.root)
        return res

    # Обход в ширину по уровням (BFS)
    def level_order(self) -> list:
        if not self.root:
            return []
        res = []
        q = deque([self.root])
        while q:
            n = q.popleft()
            res.append(n.value)
            if n.left:
                q.append(n.left)
            if n.right:
                q.append(n.right)
        return res

    # Высота дерева
    def height(self, node=None) -> int:
        if node is None:
            node = self.root
        if not node:
            return 0
        lh = self.height(node.left) if node.left else 0
        rh = self.height(node.right) if node.right else 0
        return 1 + max(lh, rh)

    # Визуализация дерева в консоли
    def print_tree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root
        if not node:
            print("<дерево пусто>")
            return
        if node.right:
            self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.value))
        if node.left:
            self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

def run_all_demo():
    bst = BinarySearchTree()
    vals = [50, 30, 70, 20, 40, 60, 80]
    print(f"\n1. Добавление элементов в BST: {vals}\n")
    for v in vals:
        bst.insert(v)

    print("2. Структура дерева:")
    bst.print_tree()

    print("\n3. Алгоритмы обхода дерева:")
    print(f"  Прямой (Pre-order):         {bst.pre_order()}")
    print(f"  Симметричный (In-order):    {bst.in_order()}")
    print(f"  Обратный (Post-order):      {bst.post_order()}")
    print(f"  В ширину (Level-order/BFS): {bst.level_order()}")
    print(f"\n4. Высота дерева: {bst.height()}")
    print(f"5. Поиск 40: {'найден' if bst.search(40) else 'НЕ найден'}; 99: {'найден' if bst.search(99) else 'НЕ найден'}")

def run_interactive():
    print("\nВведите числа через пробел для построения двоичного дерева поиска (BST):")
    vals = input_list_int("Числа", "50 30 70 20 40 60 80")
    bst = BinarySearchTree()
    for v in vals:
        bst.insert(v)

    print("\n-> Структура построенного дерева:")
    bst.print_tree()

    print("\n-> Результаты обходов дерева:")
    print(f"  Прямой (Pre-order):         {bst.pre_order()}")
    print(f"  Симметричный (In-order):    {bst.in_order()}")
    print(f"  Обратный (Post-order):      {bst.post_order()}")
    print(f"  В ширину (Level-order/BFS): {bst.level_order()}")
    print(f"  Высота дерева:              {bst.height()}")

    target = input_int("Введите число для поиска в дереве", 40)
    found = bst.search(target)
    print(f"-> Поиск {target}: {'найдено в дереве!' if found else 'НЕ найдено'}")

def main():
    print("=" * 60)
    print("Лабораторная работа №11: Работа с деревьями")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    print("\nВыберите режим работы:")
    print("1 - Запустить демонстрацию со стандартным деревом")
    print("2 - Ввести свой набор чисел для построения дерева")
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

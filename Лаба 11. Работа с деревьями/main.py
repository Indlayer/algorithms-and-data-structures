from collections import deque

class TreeNode:
    """Узел бинарного дерева."""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    """Бинарное дерево поиска (BST) с методами вставки, поиска и различных обходов."""
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Вставка значения в дерево поиска."""
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
        # Если значение уже существует, дубликаты опускаем или не добавляем

    def search(self, value) -> bool:
        """Поиск значения в дереве."""
        curr = self.root
        while curr:
            if curr.value == value:
                return True
            elif value < curr.value:
                curr = curr.left
            else:
                curr = curr.right
        return False

    def pre_order(self) -> list:
        """Прямой обход (Pre-order): Корень -> Левый -> Правый."""
        res = []
        def _walk(node):
            if node:
                res.append(node.value)
                _walk(node.left)
                _walk(node.right)
        _walk(self.root)
        return res

    def in_order(self) -> list:
        """Симметричный / центрированный обход (In-order): Левый -> Корень -> Правый."""
        res = []
        def _walk(node):
            if node:
                _walk(node.left)
                res.append(node.value)
                _walk(node.right)
        _walk(self.root)
        return res

    def post_order(self) -> list:
        """Обратный обход (Post-order): Левый -> Правый -> Корень."""
        res = []
        def _walk(node):
            if node:
                _walk(node.left)
                _walk(node.right)
                res.append(node.value)
        _walk(self.root)
        return res

    def level_order(self) -> list:
        """Обход в ширину / по уровням (Level-order / BFS)."""
        if not self.root:
            return []
        res = []
        q = deque([self.root])
        while q:
            node = q.popleft()
            res.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return res

    def height(self, node=None) -> int:
        """Вычисление высоты дерева."""
        if node is None:
            node = self.root
        if not node:
            return 0
        left_h = self.height(node.left) if node.left else 0
        right_h = self.height(node.right) if node.right else 0
        return 1 + max(left_h, right_h)

    def print_tree(self, node=None, prefix="", is_left=True):
        """Псевдографическая печать структуры дерева в консоли."""
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

def main():
    print("=" * 60)
    print("Лабораторная работа №11: Работа с деревьями")
    print("Выполнил: студент Белов Тимофей Константинович, группа 243-321")
    print("=" * 60)

    bst = BinarySearchTree()
    values = [50, 30, 70, 20, 40, 60, 80]
    print(f"1. Добавление элементов в BST: {values}\n")
    for v in values:
        bst.insert(v)

    print("2. Структура дерева в консоли:")
    bst.print_tree()
    print()

    # Обходы
    print("3. Алгоритмы обхода дерева:")
    print(f"  а) Прямой обход (Pre-order, Корень-Левый-Правый):   {bst.pre_order()}")
    print(f"  б) Центрированный (In-order, отсортированный):       {bst.in_order()}")
    print(f"  в) Обратный обход (Post-order, Левый-Правый-Корень): {bst.post_order()}")
    print(f"  г) Обход в ширину (Level-order / BFS):             {bst.level_order()}")

    print(f"\n4. Высота дерева: {bst.height()}")

    # Поиск
    print("\n5. Поиск элементов:")
    for target in [40, 99]:
        found = bst.search(target)
        status = "найден" if found else "НЕ найден"
        print(f"  Элемент {target}: {status}")

    print("=" * 60)

if __name__ == "__main__":
    main()

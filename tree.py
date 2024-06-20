from node import Node

#дерево
class Tree:
    def __init__(self):
        self.root = None

    # поиск узла:
    def __find(self, node, parent, value):
        if node is None:
            return None, parent, False
        if value == node.data:
            return node, parent, True
        if value < node.data:
            if node.left:
                return self.__find(node.left, node, value)
        if value > node.data:
            if node.right:
                return self.__find(node.right, node, value)
        return node, parent, False

    # добавление узла
    def append(self, obj):
        if self.root is None:
            self.root = obj
            return obj
        
        s, p, fl_find = self.__find(self.root,None, obj.data)
        if not fl_find and s:

            if obj.data < s.data:
                s.left = obj
            else:
                s.right = obj

        return obj

    # рекурсивно показат дерево
    def show_tree(self, node):
        if node is None:
            return
        self.show_tree(node.right)

        print(node.data)

        self.show_tree(node.left)

    # показать дерево (по уровням)
    def show_wide_tree(self, node):
        if node is None:
            return
        
        v = [node]

        while v:
            vn = []

            for x in v:

                print(x.data, end=" ")
                if x.left:
                    vn += [x.left]

                if x.right:
                    vn += [x.right]

            print()
            v = vn

    # удаление листа
    def __del_leaf(self, s, p):
        if p.left == s:
            p.left = None

        elif p.right == s:
            p.right = None

    # удаление узла с одним ребенком
    def __del_one_child(self, s, p):
        if p.left == s:
            if s.left is None:
                p.left = s.right

            elif s.right is None:
                p.left = s.left

        elif p.right == s:
            if s.left is None:
                p.right = s.right

            elif s.right is None:
                p.right = s.left

    # найти минимальный узел
    def __find_min(self, node, parent):
        if node.left:
            return self.__find_min(node.left, node)
        return node, parent

    # удалениие узла
    def del_node(self, key):
        s, p, fl_find = self.__find(self.root, None, key)

        if not fl_find:
            return None
        
        if s.left is None and s.right is None:
            self.__del_leaf(s, p)

        elif s.left is None or s.right is None:
            self.__del_one_child(s, p)
            
        else:
            sr, pr = self.__find_min(s.right, s)
            s.data = sr.data
            self.__del_one_child(sr, pr)

    # обход КЛП
    def klp(self, node, result):
        if node:
            result.append(node.data)
            self.klp(node.left, result)
            self.klp(node.right, result)

    # КПЛ
    def kpl(self, node, result):
        if node:
            result.append(node.data)
            self.kpl(node.right, result)
            self.kpl(node.left, result)

    # ЛПК
    def lpk(self, node, result):
        if node:
            self.lpk(node.left, result)
            self.lpk(node.right, result)
            result.append(node.data)

    #ЛКП
    def lkp(self, node, result):
        if node:
            self.lkp(node.left, result)
            result.append(node.data)
            self.lkp(node.right, result)

    # ПЛК
    def plk(self, node, result):
        if node:
            self.plk(node.right, result)
            self.plk(node.left, result)
            result.append(node.data)

    # ПКЛ
    def pkl(self, node, result):
        if node:
            self.pkl(node.right, result)
            result.append(node.data)
            self.pkl(node.left, result)

    # сохранение дерева
    def save_tree(self, traversal_type='klp'):
        result = []
        traversal_method = getattr(self, traversal_type.lower())
        traversal_method(self.root, result)
        return ' '.join(map(str, result))

    # загрузка дерева
    def load_tree(self, data, traversal_type='klp'):
        values = list(map(int, data.split()))
        self.root = None
        for value in values:

            self.append(Node(value))

    # построение нового дерева по элементному преобразованию
    def map(self, func):
        new_tree = Tree()

        self.__map_recursive(self.root, new_tree, func)
        return new_tree

    # рекурсивная часть map
    def __map_recursive(self, node, new_tree, func):
        if node:
            new_tree.append(Node(func(node.data)))
            self.__map_recursive(node.left, new_tree, func)
            self.__map_recursive(node.right, new_tree, func)

    # построение нового дерева по условию
    def where(self, predicate):
        new_tree = Tree()
        self.__where_recursive(self.root, new_tree, predicate)
        return new_tree

    # рекурсивная часть where
    def __where_recursive(self, node, new_tree, predicate):
        if node:
            if predicate(node.data):
                new_tree.append(Node(node.data))
            self.__where_recursive(node.left, new_tree, predicate)
            self.__where_recursive(node.right, new_tree, predicate)

    # слияние деревьев
    def merge(self, other_tree):
        new_tree = Tree()

        self.__merge_recursive(self.root, new_tree)

        self.__merge_recursive(other_tree.root, new_tree)

        return new_tree

    # рекурсивная часть merge
    def __merge_recursive(self, node, new_tree):
        if node:
            new_tree.append(Node(node.data))
            self.__merge_recursive(node.left, new_tree)
            self.__merge_recursive(node.right, new_tree)

    # извлечние поддерева
    def extract_subtree(self, value):
        node, _, found = self.__find(self.root, None, value)
        if found:
            new_tree = Tree()
            new_tree.root = node
            return new_tree
        return None

    # поиск поддерева
    def search_subtree(self, subtree):
        def is_identical(node1, node2):
            if not node1 and not node2:
                return True
            if node1 and node2 and node1.data == node2.data:
                return is_identical(node1.left, node2.left) and is_identical(node1.right, node2.right)
            return False
        return self.__search_subtree_recursive(self.root, subtree.root, is_identical)

    # рекурсивная часть search_subtree
    def __search_subtree_recursive(self, node, sub_root, is_identical):
        if not node:
            return False
        if is_identical(node, sub_root):
            return True
        return self.__search_subtree_recursive(node.left, sub_root, is_identical) or \
               self.__search_subtree_recursive(node.right, sub_root, is_identical)

    #поиск элемента
    def search_element(self, value):
        _, _, found = self.__find(self.root, None, value)
        return found

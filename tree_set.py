from tree import Tree
from node import Node

# Множество на основе дерева
class TreeSet:
    def __init__(self):
        self.tree = Tree()

    # построение нового множества 
    def map(self, func):

        new_set = TreeSet()

        new_set.tree = self.tree.map(func)
        return new_set

    # построение нового множества по условию
    def where(self, predicate):
        new_set = TreeSet()
        new_set.tree = self.tree.where(predicate)
        return new_set

    # объединение множеств
    def union(self, other):
        new_set = TreeSet()
        new_set.tree = self.tree.merge(other.tree)
        return new_set

    # пересечние множеств
    def intersection(self, other):
        new_set = TreeSet()
        for value in self.to_list():
            if other.contains(value):
                new_set.add(value)
        return new_set

    # вычитание множеств

    def difference(self, other):
        new_set = TreeSet()
        for value in self.to_list():
            if not other.contains(value):
                new_set.add(value)
        return new_set

    # проверка на включение подмножества
    def is_subset(self, other):
        for value in self.to_list():
            if not other.contains(value):
                return False
        return True

    # проверка на вхождение элемента

    def contains(self, value):
        return self.tree.search_element(value)

    # добавление элемента
    def add(self, value):

        self.tree.append(Node(value))

    # преобразование в список
    def to_list(self):
        result = []
        self.tree.klp(self.tree.root, result)
        return result

    # сравнение множеств
    def __eq__(self, other):
        return set(self.to_list()) == set(other.to_list())

    # сохранение множества
    def save_set(self):
        return self.tree.save_tree()

    # загрузка множества
    def load_set(self, data):
        self.tree.load_tree(data)

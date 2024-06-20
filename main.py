# UI

from node import Node
from tree import Tree
from tree_set import TreeSet
from function import Function
from student import Student
from teacher import Teacher


def main():
    print("Выберите действие:")
    print("1. Работа с деревом")
    print("2. Работа с множеством")
    choice = int(input("Введите номер действия: "))

    if choice == 1:
        tree = Tree()
        while True:
            print("\n1. Добавить элемент")
            print("2. Показать дерево")
            print("3. Удалить элемент")
            print("4. Обход дерева")
            print("5. Сохранить дерево")
            print("6. Загрузить дерево")
            print("7. Выйти")
            action = int(input("Введите номер действия: "))

            if action == 1:
                value = input("Введите значение (целое число): ")
                tree.append(Node(int(value)))
            elif action == 2:
                print("Дерево (по уровням):")
                tree.show_wide_tree(tree.root)
            elif action == 3:
                value = input("Введите значение для удаления: ")
                tree.del_node(int(value))
            elif action == 4:
                print("Выберите тип обхода:")
                print("1. KLP")
                print("2. КПЛ")
                print("3. ЛПК")
                print("4. ЛКП")
                print("5. ПЛК")
                print("6. ПКЛ")
                traversal_type = int(input("Введите номер обхода: "))
                result = []
                if traversal_type == 1:
                    tree.klp(tree.root, result)
                elif traversal_type == 2:
                    tree.kpl(tree.root, result)
                elif traversal_type == 3:
                    tree.lpk(tree.root, result)
                elif traversal_type == 4:
                    tree.lkp(tree.root, result)
                elif traversal_type == 5:
                    tree.plk(tree.root, result)
                elif traversal_type == 6:
                    tree.pkl(tree.root, result)
                print("Результат обхода:", result)
            elif action == 5:
                traversal_type = input("Введите тип обхода для сохранения (klp, kpl, lpk, lkp, plk, pkl): ")
                data = tree.save_tree(traversal_type)
                print("Сохраненные данные:", data)
            elif action == 6:
                data = input("Введите данные для загрузки: ")
                traversal_type = input("Введите тип обхода для загрузки (klp, kpl, lpk, lkp, plk, pkl): ")
                tree.load_tree(data, traversal_type)
            elif action == 7:
                break

    elif choice == 2:
        tree_set = TreeSet()
        while True:
            print("\n1. Добавить элемент")
            print("2. Показать множество")
            print("3. Проверка на вхождение элемента")
            print("4. Сохранить множество")
            print("5. Загрузить множество")
            print("6. Объединение множеств")
            print("7. Пересечение множеств")
            print("8. Вычитание множеств")
            print("9. Проверка на подмножество")
            print("10. Выйти")
            action = int(input("Введите номер действия: "))

            if action == 1:
                value = input("Введите значение : ")
                tree_set.add(value)
            elif action == 2:
                print("Множество:", tree_set.to_list())
            elif action == 3:
                value = input("Введите значение для проверки: ")
                print("Элемент", "найден" if tree_set.contains(value) else "не найден")
            elif action == 4:
                data = tree_set.save_set()
                print("Сохраненные данные:", data)
            elif action == 5:
                data = input("Введите данные для загрузки: ")
                tree_set.load_set(data)
            elif action == 6:
                other_set = TreeSet()
                other_data = input("Введите элементы другого множества через пробел: ")
                for value in map(int, other_data.split()):
                    other_set.add(value)
                union_set = tree_set.union(other_set)
                print("Объединенное множество:", union_set.to_list())
            elif action == 7:
                other_set = TreeSet()
                other_data = input("Введите элементы другого множества через пробел: ")
                for value in map(int, other_data.split()):
                    other_set.add(value)
                intersection_set = tree_set.intersection(other_set)
                print("Пересечение множеств:", intersection_set.to_list())
            elif action == 8:
                other_set = TreeSet()
                other_data = input("Введите элементы другого множества через пробел: ")
                for value in map(int, other_data.split()):
                    other_set.add(value)
                difference_set = tree_set.difference(other_set)
                print("Разность множеств:", difference_set.to_list())
            elif action == 9:
                other_set = TreeSet()
                other_data = input("Введите элементы другого множества через пробел: ")
                for value in map(int, other_data.split()):
                    other_set.add(value)
                print("Это подмножество" if tree_set.is_subset(other_set) else "Это не подмножество")
            elif action == 10:
                break

if __name__ == "__main__":
    main()

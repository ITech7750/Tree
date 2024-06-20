# Автотесты

import unittest
from node import Node
from tree import Tree
from tree_set import TreeSet
from function import Function
from student import Student
from teacher import Teacher

class TestTree(unittest.TestCase):
    def test_append_and_search(self):
        tree = Tree()
        tree.append(Node(10))
        tree.append(Node(5))
        tree.append(Node(15))

        self.assertTrue(tree.search_element(10))
        self.assertTrue(tree.search_element(5))
        self.assertTrue(tree.search_element(15))
        self.assertFalse(tree.search_element(20))

    def test_delete(self):
        tree = Tree()
        tree.append(Node(10))
        tree.append(Node(5))
        tree.append(Node(15))
        tree.del_node(5)

        self.assertFalse(tree.search_element(5))

    def test_save_and_load(self):
        tree = Tree()
        tree.append(Node(10))
        tree.append(Node(5))
        tree.append(Node(15))

        data = tree.save_tree('klp')
        new_tree = Tree()
        new_tree.load_tree(data, 'klp')
        self.assertTrue(new_tree.search_element(10))
        self.assertTrue(new_tree.search_element(5))
        self.assertTrue(new_tree.search_element(15))

    def test_map(self):
        tree = Tree()
        tree.append(Node(10))
        tree.append(Node(5))
        tree.append(Node(15))

        new_tree = tree.map(lambda x: x * 2)

        self.assertTrue(new_tree.search_element(20))
        self.assertTrue(new_tree.search_element(10))
        self.assertTrue(new_tree.search_element(30))

    def test_where(self):
        tree = Tree()
        tree.append(Node(10))
        tree.append(Node(5))
        tree.append(Node(15))
        new_tree = tree.where(lambda x: x > 10)


        self.assertFalse(new_tree.search_element(10))
        self.assertFalse(new_tree.search_element(5))
        self.assertTrue(new_tree.search_element(15))

class TestTreeSet(unittest.TestCase):
    def test_add_and_contains(self):
        tree_set = TreeSet()
        tree_set.add(10)
        tree_set.add(5)
        tree_set.add(15)

        self.assertTrue(tree_set.contains(10))
        self.assertTrue(tree_set.contains(5))
        self.assertTrue(tree_set.contains(15))

        self.assertFalse(tree_set.contains(20))

    def test_save_and_load(self):
        tree_set = TreeSet()

        tree_set.add(10)
        tree_set.add(5)
        tree_set.add(15)
        data = tree_set.save_set()

        new_set = TreeSet()
        new_set.load_set(data)
        self.assertTrue(new_set.contains(10))
        self.assertTrue(new_set.contains(5))
        self.assertTrue(new_set.contains(15))

    def test_union(self):
        set1 = TreeSet()
        set1.add(10)
        set1.add(5)
        set1.add(15)

        set2 = TreeSet()
        set2.add(20)

        set2.add(10)
        union_set = set1.union(set2)
        self.assertTrue(union_set.contains(10))
        self.assertTrue(union_set.contains(5))
        self.assertTrue(union_set.contains(15))
        self.assertTrue(union_set.contains(20))

    def test_intersection(self):
        set1 = TreeSet()
        set1.add(10)
        set1.add(5)
        set1.add(15)
        set2 = TreeSet()

        set2.add(20)
        set2.add(10)
        intersection_set = set1.intersection(set2)

        self.assertTrue(intersection_set.contains(10))
        self.assertFalse(intersection_set.contains(5))
        self.assertFalse(intersection_set.contains(15))
        self.assertFalse(intersection_set.contains(20))

    def test_difference(self):
        set1 = TreeSet()
        set1.add(10)
        set1.add(5)
        set1.add(15)

        set2 = TreeSet()

        set2.add(20)
        set2.add(10)
        difference_set = set1.difference(set2)
        self.assertFalse(difference_set.contains(10))
        self.assertTrue(difference_set.contains(5))
        self.assertTrue(difference_set.contains(15))
        self.assertFalse(difference_set.contains(20))

if __name__ == '__main__':
    unittest.main()

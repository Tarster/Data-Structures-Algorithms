import sys
sys.path.append(r'Python\LinkedList')

from linked_list import LinkedList
import unittest

class LinkedListTest(unittest.TestCase):
    

    def test_add(self):
        print("Test Add")
        my_list = LinkedList()
        my_list.add(5)
        my_list.add(10)
        my_list.add(15)
        my_list.add(20)
        my_list.add(25)
        my_list.print_list()
    
    def test_remove(self):
        print("Test Remove")
        my_list = LinkedList()
        my_list.add(5)
        my_list.add(10)
        my_list.add(15)
        my_list.add(20)
        my_list.add(25)
        my_list.print_list()
        my_list.remove(10)
        my_list.print_list()
    
    def test_find(self):
        print("Test Find")
        my_list = LinkedList()
        my_list.add(5)
        my_list.add(10)
        my_list.add(15)
        my_list.add(20)
        my_list.add(25)
        my_list.print_list()
        print(my_list.find(10))


if __name__ == "__main__":
    unittest.main()
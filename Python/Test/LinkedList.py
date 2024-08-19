import sys
sys.path.append(r'Python\LinkedList')

from linked_list import LinkedList
from double_linked_list import DoubleLinkedList
from circular_linked_list import CircularLinkedList
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

class DoubleLinkedListTest(unittest.TestCase):
    def test_add(self):
        print("Testing Add")
        my_list = DoubleLinkedList()
        my_list.add(1)
        my_list.add(2)
        my_list.add(10, place="front")
        my_list.add(8, place="front")
        my_list.printDoubleList()

    def test_print(self):
        print("Testing Print")
        my_list = DoubleLinkedList()
        my_list.add(1)
        my_list.add(2)
        my_list.add(10, place="front")
        my_list.add(8, place="front")
        my_list.printDoubleList()
        my_list.printDoubleList(place="back")

    def test_find(self):
        print("Testing find")
        my_list = DoubleLinkedList()
        my_list.add(1)
        my_list.add(2)
        my_list.add(10, place="front")
        my_list.add(8, place="front")
        print(my_list.find(8))
        print(my_list.find(25))
        # my_list.printDoubleList()

    def test_delete(self):
        print("Testing Delete")
        my_list = DoubleLinkedList()
        my_list.add(1)
        my_list.add(2)
        print(my_list.delete(1))
        my_list.printDoubleList() # print just 2
        
        my_list.add(1, place="front")
        my_list.printDoubleList() # print 1 and 2
        
        print(my_list.delete(2))
        my_list.printDoubleList() # print 1

        print(my_list.delete(1))
        my_list.printDoubleList() # Nothing


        my_list.add(20, place="front")
        my_list.add(10, place="front")
        my_list.add(8, place="front")
        my_list.printDoubleList() # print 20, 10, 8
        print(my_list.delete(20))
        my_list.printDoubleList() # print 20, 8


class CircularLinkedListTest(unittest.TestCase):
    def test_add(self):
        print("Testing Add function")
        my_list = CircularLinkedList()
        my_list.add(4)
        my_list.add(2)
        my_list.add(6)
        my_list.add(9, pos="back")
        my_list.print_list()
    
    def test_find(self):
        print("Testing Find function")
        my_list = CircularLinkedList()
        my_list.add(4)
        my_list.add(2)
        my_list.add(6)
        my_list.add(9, pos="back")
        print(my_list.find(6))
        print(my_list.find(100))
        # my_list.print_list()

    def test_delete(self):
        print("Testing Delete function")
        my_list = CircularLinkedList()
        my_list.add(4)
        my_list.add(2)
        my_list.add(6)
        my_list.add(9, pos="back")
        
        # Delete last
        print(my_list.delete(9))
        my_list.print_list()
        
        # Delete First
        print(my_list.delete(6))
        my_list.print_list()
        # Delete middle 
        my_list.add(100) 
        print(my_list.delete(2))
        my_list.print_list()

        # Value not present
        print(my_list.delete(400))
        
        # Delete everything
        print(my_list.delete(4))
        my_list.print_list()
        
        print(my_list.delete(100))
        my_list.print_list()
        
        # Empty list delete
        print(my_list.delete(3))
        my_list.print_list()


def run_some_tests():
    test_class_to_test = [
                    LinkedListTest, 
                    DoubleLinkedListTest,
                    CircularLinkedListTest
                          ] # comment classes here to test individual classes

    loader = unittest.TestLoader()

    suites_list = []

    for test_class in test_class_to_test:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    # print(suites_list)

    big_suite = unittest.TestSuite(suites_list)
    
    runner = unittest.TextTestRunner()
    results = runner.run(big_suite)


if __name__ == "__main__":
    run_some_tests()
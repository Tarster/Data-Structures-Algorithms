import sys
import unittest
sys.path.append(r'Python\LinkedList')
sys.path.append(r'Python\Test\LinkedListTest')

from CircularLinkedListTest import CircularLinkedListTest
from DoubleLinkedListTest import DoubleLinkedListTest
from LinkedListTest import LinkedListTest
from StackTest import SimpleStackTest

        
def run_some_tests():
    test_class_to_test = [
                    # LinkedListTest, 
                    # DoubleLinkedListTest,
                    # CircularLinkedListTest,
                    SimpleStackTest
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
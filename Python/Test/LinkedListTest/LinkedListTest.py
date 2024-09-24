import unittest
from linked_list import LinkedList


class LinkedListTest(unittest.TestCase):
    
    # Test Case: Adding elements to the list
    def test_add(self):
        my_list = LinkedList()
        
        # Add elements to an empty list
        my_list.add(5)
        self.assertEqual(my_list.root.get_data(), 5)
        
        # Add more elements
        my_list.add(10)
        my_list.add(15)
        expected = [15, 10, 5]  # Since the list is added in LIFO order
        self.assertEqual(my_list.to_list(), expected)
    
    # Test Case: Removing elements from the list
    def test_remove(self):
        my_list = LinkedList()
        
        # Add elements
        my_list.add(5)
        my_list.add(10)
        my_list.add(15)
        
        # Remove the head/root
        my_list.remove(15)
        expected = [10, 5]
        # my_list.print_list()
        self.assertEqual(my_list.to_list(), expected)
        
        # Remove the tail
        my_list.remove(5)
        expected = [10]
        self.assertEqual(my_list.to_list(), expected)
        
        # Remove from an empty list
        my_list.remove(10)  # List becomes empty
        self.assertEqual(my_list.to_list(), [])
        my_list.remove(20)  # Trying to remove from an empty list (should be no effect)
        self.assertEqual(my_list.to_list(), [])
    
    # Test Case: Finding elements in the list
    def test_find(self):
        my_list = LinkedList()
        
        # Add elements
        my_list.add(5)
        my_list.add(10)
        my_list.add(15)
        
        # Find elements
        self.assertTrue(my_list.find(10))
        self.assertFalse(my_list.find(100))  # Element not in the list
        
        # Edge Case: Find in an empty list
        empty_list = LinkedList()
        self.assertFalse(empty_list.find(10))  # Searching in an empty list
    
    # Test Case: Edge cases and boundary conditions
    def test_edge_cases(self):
        # Edge case: List with a single element
        my_list = LinkedList()
        my_list.add(1)
        self.assertEqual(my_list.root.get_data(), 1)
        
        # Try removing the only element
        my_list.remove(1)
        self.assertEqual(my_list.root, None)
        
        # Edge case: Removing non-existent element from an empty list
        my_list.remove(2)
        self.assertEqual(my_list.root, None)
        
        # Edge case: List with duplicates
        my_list.add(1)
        my_list.add(1)
        my_list.add(1)
        expected = [1, 1, 1]
        self.assertEqual(my_list.to_list(), expected)
        my_list.remove(1)  # Should remove the first occurrence
        expected = [1, 1]
        self.assertEqual(my_list.to_list(), expected)

import unittest
from double_linked_list import DoubleLinkedList

# Double Linked List Test
class DoubleLinkedListTest(unittest.TestCase):
    # Test Case: Adding elements to the back
    def test_add_back(self):
        dll = DoubleLinkedList()
        dll.add(10, place="back")
        self.assertEqual(dll.to_list(), [10])
        self.assertEqual(dll.root, dll.end)
        dll.add(20, place="back")
        self.assertEqual(dll.to_list(), [10, 20])
        self.assertNotEqual(dll.root, dll.end)
        dll.add(30, place="back")
        self.assertEqual(dll.to_list(), [10, 20, 30])

    # Test Case: Adding elements to the front
    def test_add_front(self):
        dll = DoubleLinkedList()
        dll.add(10, place="front")
        self.assertEqual(dll.to_list(), [10])
        self.assertEqual(dll.root, dll.end)
        dll.add(20, place="front")
        self.assertEqual(dll.to_list(), [20, 10])
        dll.add(30, place="front")
        self.assertEqual(dll.to_list(), [30, 20, 10])

    # Test Case: Adding elements to both front and back
    def test_add_front_back(self):
        dll = DoubleLinkedList()
        dll.add(10, place="back")
        dll.add(20, place="front")
        dll.add(30, place="back")
        dll.add(40, place="front")
        self.assertEqual(dll.to_list(), [40, 20, 10, 30])

    # Test Case: Deleting elements from the list
    def test_delete(self):
        dll = DoubleLinkedList()
        # Attempt to delete from empty list
        self.assertFalse(dll.delete(10))
        
        # Add elements
        dll.add(10, place="back")
        dll.add(20, place="back")
        dll.add(30, place="front")
        dll.add(40, place="front")  # List: [40, 30, 10, 20]
        self.assertEqual(dll.to_list(), [40, 30, 10, 20])
        
        # Delete a middle element
        self.assertTrue(dll.delete(30))
        self.assertEqual(dll.to_list(), [40, 10, 20])
        
        # Delete the root element
        self.assertTrue(dll.delete(40))
        self.assertEqual(dll.to_list(), [10, 20])
        
        # Delete the end element
        self.assertTrue(dll.delete(20))
        self.assertEqual(dll.to_list(), [10])
        
        # Delete the only remaining element
        self.assertTrue(dll.delete(10))
        self.assertEqual(dll.to_list(), [])
        
        # Attempt to delete non-existent element
        self.assertFalse(dll.delete(50))

    # Test Case: Deleting elements with duplicates
    def test_delete_duplicates(self):
        dll = DoubleLinkedList()
        dll.add(10, place="back")
        dll.add(20, place="front")
        dll.add(10, place="front")
        dll.add(30, place="back")  # List: [10, 20, 10, 30]
        self.assertEqual(dll.to_list(), [10, 20, 10, 30])
        
        # Delete first occurrence of 10 (root)
        self.assertTrue(dll.delete(10))
        self.assertEqual(dll.to_list(), [20, 10, 30])
        
        # Delete second occurrence of 10
        self.assertTrue(dll.delete(10))
        self.assertEqual(dll.to_list(), [20, 30])
        
        # Attempt to delete 10 again (no more 10s)
        self.assertFalse(dll.delete(10))
        self.assertEqual(dll.to_list(), [20, 30])

    # Test Case: Finding elements in the list
    def test_find(self):
        dll = DoubleLinkedList()
        # Find in empty list
        self.assertFalse(dll.find(10))
        
        # Add elements
        dll.add(10, place="back")
        dll.add(20, place="front")
        dll.add(30, place="back")
        dll.add(40, place="front")  # List: [40, 20, 10, 30]
        self.assertEqual(dll.to_list(), [40, 20, 10, 30])
        
        # Find existing elements
        self.assertTrue(dll.find(40))
        self.assertTrue(dll.find(20))
        self.assertTrue(dll.find(10))
        self.assertTrue(dll.find(30))
        
        # Find non-existent element
        self.assertFalse(dll.find(50))
    
    # Test Case: Edge cases and boundary conditions
    def test_edge_cases(self):
        dll = DoubleLinkedList()
        
        # Edge case: Adding and deleting a single element
        dll.add(100, place="front")
        self.assertEqual(dll.to_list(), [100])
        self.assertTrue(dll.delete(100))
        self.assertEqual(dll.to_list(), [])
        
        # Edge case: Deleting from empty list
        self.assertFalse(dll.delete(200))
        
        # Edge case: Adding multiple elements and deleting all
        dll.add(10, place="front")
        dll.add(20, place="back")
        dll.add(30, place="front")
        dll.add(40, place="back")  # List: [30, 10, 20, 40]
        self.assertEqual(dll.to_list(), [30, 10, 20, 40])
        
        self.assertTrue(dll.delete(30))
        self.assertTrue(dll.delete(10))
        self.assertTrue(dll.delete(20))
        self.assertTrue(dll.delete(40))
        self.assertEqual(dll.to_list(), [])

    # Test Case: Converting to list
    def test_to_list(self):
        dll = DoubleLinkedList()
        # Empty list
        self.assertEqual(dll.to_list(), [])
        
        # Add elements
        dll.add(1, place="back")
        dll.add(2, place="front")
        dll.add(3, place="back")
        dll.add(4, place="front")  # List: [4, 2, 1, 3]
        self.assertEqual(dll.to_list(), [4, 2, 1, 3])
        
        # Delete an element and check
        dll.delete(2)  # List should be [4, 1, 3]
        self.assertEqual(dll.to_list(), [4, 1, 3])
        
    # Test Case: Ensuring the integrity of previous and next pointers
    def test_pointers(self):
        dll = DoubleLinkedList()
        dll.add(10, place="back")
        dll.add(20, place="back")
        dll.add(30, place="front")  # List: [30, 10, 20]
        
        # Check root and end
        self.assertEqual(dll.root.get_data(), 30)
        self.assertEqual(dll.end.get_data(), 20)
        
        # Check previous and next pointers
        self.assertIsNone(dll.root.get_prev())
        self.assertEqual(dll.root.get_next().get_data(), 10)
        self.assertEqual(dll.end.get_prev().get_data(), 10)
        self.assertIsNone(dll.end.get_next())
        
        # Intermediate node
        middle_node = dll.root.get_next()
        self.assertEqual(middle_node.get_data(), 10)
        self.assertEqual(middle_node.get_prev().get_data(), 30)
        self.assertEqual(middle_node.get_next().get_data(), 20)
    
    # Test Case: Adding elements without specifying the place (default to back)
    def test_add_default_back(self):
        dll = DoubleLinkedList()
        dll.add(10)
        self.assertEqual(dll.to_list(), [10])
        dll.add(20)
        self.assertEqual(dll.to_list(), [10, 20])
        dll.add(30)
        self.assertEqual(dll.to_list(), [10, 20, 30])
    
    # Test Case: Adding elements with None as data
    def test_add_none_data(self):
        dll = DoubleLinkedList()
        dll.add()
        self.assertEqual(dll.to_list(), [None])
        dll.add(10, place="front")
        self.assertEqual(dll.to_list(), [10, None])
        dll.add(None, place="back")
        self.assertEqual(dll.to_list(), [10, None, None])

    # Test Case: Deleting elements with None as data
    def test_delete_none_data(self):
        dll = DoubleLinkedList()
        dll.add(None, place="back")
        dll.add(10, place="front")
        dll.add(None, place="back")  # List: [10, None, None]
        self.assertEqual(dll.to_list(), [10, None, None])
        
        # Delete first occurrence of None
        self.assertTrue(dll.delete(None))
        self.assertEqual(dll.to_list(), [10, None])
        
        # Delete second occurrence of None
        self.assertTrue(dll.delete(None))
        self.assertEqual(dll.to_list(), [10])
        
        # Attempt to delete None again
        self.assertFalse(dll.delete(None))
        self.assertEqual(dll.to_list(), [10])

    # Test Case: Ensuring list size is maintained correctly
    def test_size(self):
        dll = DoubleLinkedList()
        self.assertEqual(dll.size, 0)
        dll.add(10)
        self.assertEqual(dll.size, 1)
        dll.add(20, place="front")
        self.assertEqual(dll.size, 2)
        dll.add(30, place="back")
        self.assertEqual(dll.size, 3)
        dll.delete(20)
        self.assertEqual(dll.size, 2)
        dll.delete(10)
        self.assertEqual(dll.size, 1)
        dll.delete(30)
        self.assertEqual(dll.size, 0)

    # Test Case: Ensuring no memory leaks or orphaned nodes (conceptual, as Python has garbage collection)
    def test_no_orphaned_nodes(self):
        dll = DoubleLinkedList()
        dll.add(10)
        dll.add(20)
        dll.add(30)
        dll.delete(20)
        self.assertEqual(dll.to_list(), [10, 30])
        # There's no direct way to test for memory leaks in Python, but ensuring the links are correct
        self.assertEqual(dll.root.get_next().get_data(), 30)
        self.assertEqual(dll.end.get_prev().get_data(), 10)

    # Test Case: Adding and deleting multiple elements
    def test_multiple_operations(self):
        dll = DoubleLinkedList()
        operations = [
            ('add', 10, 'back'),
            ('add', 20, 'front'),
            ('add', 30, 'back'),
            ('delete', 20, None),
            ('add', 40, 'front'),
            ('delete', 10, None),
            ('add', 50, 'back'),
            ('delete', 60, None),  # Non-existent
            ('add', 60, 'front'),
            ('delete', 30, None),
        ]
        expected_lists = [
            [10],               # After adding 10 to back
            [20, 10],           # After adding 20 to front
            [20, 10, 30],       # After adding 30 to back
            [10, 30],           # After deleting 20
            [40, 10, 30],       # After adding 40 to front
            [40, 30],           # After deleting 10
            [40, 30, 50],       # After adding 50 to back
            [40, 30, 50],       # After attempting to delete 60 (non-existent)
            [60, 40, 30, 50],   # After adding 60 to front
            [60, 40, 50],       
        ]
        for i, (op, data, place) in enumerate(operations):
            if op == 'add':
                dll.add(data, place)
            elif op == 'delete':
                dll.delete(data)
            self.assertEqual(dll.to_list(), expected_lists[i])

    # Test Case: Ensuring proper linkage after multiple additions and deletions
    def test_linkage_integrity(self):
        dll = DoubleLinkedList()
        dll.add(10, place="back")
        dll.add(20, place="back")
        dll.add(30, place="front")  # List: [30, 10, 20]
        
        # Delete the middle node
        dll.delete(10)  # List: [30, 20]
        self.assertEqual(dll.to_list(), [30, 20])
        self.assertEqual(dll.root.get_next().get_data(), 20)
        self.assertEqual(dll.end.get_prev().get_data(), 30)
        
        # Add another node to front
        dll.add(40, place="front")  # List: [40, 30, 20]
        self.assertEqual(dll.to_list(), [40, 30, 20])
        self.assertEqual(dll.root.get_next().get_data(), 30)
        self.assertEqual(dll.end.get_prev().get_data(), 30)
        
        # Delete end node
        dll.delete(20)  # List: [40, 30]
        self.assertEqual(dll.to_list(), [40, 30])
        self.assertEqual(dll.end.get_prev().get_data(), 40)
        self.assertIsNone(dll.end.get_next())

    # Test Case: Handling multiple identical elements
    def test_multiple_identical_elements(self):
        dll = DoubleLinkedList()
        dll.add(10, place="back")
        dll.add(10, place="back")
        dll.add(10, place="front")  # List: [10, 10, 10]
        self.assertEqual(dll.to_list(), [10, 10, 10])
        
        # Delete first occurrence (root)
        self.assertTrue(dll.delete(10))
        self.assertEqual(dll.to_list(), [10, 10])
        
        # Delete second occurrence (new root)
        self.assertTrue(dll.delete(10))
        self.assertEqual(dll.to_list(), [10])
        
        # Delete last occurrence
        self.assertTrue(dll.delete(10))
        self.assertEqual(dll.to_list(), [])
        
        # Attempt to delete when list is empty
        self.assertFalse(dll.delete(10))

    # Test Case: Ensuring the list behaves correctly when adding and deleting alternately
    def test_alternating_add_delete(self):
        dll = DoubleLinkedList()
        dll.add(10, place="back")   # [10]
        dll.delete(10)               # []
        self.assertEqual(dll.to_list(), [])
        dll.add(20, place="front")  # [20]
        self.assertEqual(dll.to_list(), [20])
        dll.add(30, place="back")   # [20, 30]
        self.assertEqual(dll.to_list(), [20, 30])
        dll.delete(20)               # [30]
        self.assertEqual(dll.to_list(), [30])
        dll.add(40, place="front")  # [40, 30]
        self.assertEqual(dll.to_list(), [40, 30])
        dll.delete(30)               # [40]
        self.assertEqual(dll.to_list(), [40])
        dll.delete(40)               # []
        self.assertEqual(dll.to_list(), [])

    # Test Case: Ensuring that adding elements without specifying 'place' defaults to 'back'
    def test_add_default_place(self):
        dll = DoubleLinkedList()
        dll.add(10)
        self.assertEqual(dll.to_list(), [10])
        dll.add(20)
        self.assertEqual(dll.to_list(), [10, 20])
        dll.add(30)
        self.assertEqual(dll.to_list(), [10, 20, 30])

    # Test Case: Ensuring that the list size updates correctly
    def test_size_updates(self):
        dll = DoubleLinkedList()
        self.assertEqual(dll.size, 0)
        dll.add(10)
        self.assertEqual(dll.size, 1)
        dll.add(20, place="front")
        self.assertEqual(dll.size, 2)
        dll.add(30)
        self.assertEqual(dll.size, 3)
        dll.delete(20)
        self.assertEqual(dll.size, 2)
        dll.delete(10)
        self.assertEqual(dll.size, 1)
        dll.delete(30)
        self.assertEqual(dll.size, 0)

    # Test Case: Adding and deleting multiple elements to check the integrity of previous and next links
    def test_integrity_after_operations(self):
        dll = DoubleLinkedList()
        dll.add(10, place="back")
        dll.add(20, place="back")
        dll.add(30, place="front")  # List: [30, 10, 20]
        dll.add(40, place="front")  # List: [40, 30, 10, 20]
        self.assertEqual(dll.to_list(), [40, 30, 10, 20])
        
        # Delete middle element
        dll.delete(30)  # List: [40, 10, 20]
        self.assertEqual(dll.to_list(), [40, 10, 20])
        
        # Check previous and next pointers
        self.assertEqual(dll.root.get_data(), 40)
        self.assertEqual(dll.root.get_next().get_data(), 10)
        self.assertEqual(dll.root.get_next().get_prev().get_data(), 40)
        self.assertEqual(dll.end.get_prev().get_data(), 10)
        self.assertEqual(dll.end.get_prev().get_next().get_data(), 20)
        self.assertIsNone(dll.end.get_next())

    # Test Case: Handling None as data
    def test_handling_none_data(self):
        dll = DoubleLinkedList()
        dll.add(None, place="back")
        self.assertEqual(dll.to_list(), [None])
        dll.add(10, place="front")
        self.assertEqual(dll.to_list(), [10, None])
        dll.add(None, place="front")
        self.assertEqual(dll.to_list(), [None, 10, None])
        
        # Delete first occurrence of None
        self.assertTrue(dll.delete(None))
        self.assertEqual(dll.to_list(), [10, None])
        
        # Delete second occurrence of None
        self.assertTrue(dll.delete(None))
        self.assertEqual(dll.to_list(), [10])
        
        # Attempt to delete None again
        self.assertFalse(dll.delete(None))
        self.assertEqual(dll.to_list(), [10])

    # Test Case: Ensuring that deleting a node correctly updates the links
    def test_link_updates_on_delete(self):
        dll = DoubleLinkedList()
        dll.add(10, place="back")
        dll.add(20, place="back")
        dll.add(30, place="back")  # List: [10, 20, 30]
        
        # Delete the middle node (20)
        self.assertTrue(dll.delete(20))
        self.assertEqual(dll.to_list(), [10, 30])
        # Ensure that 10's next is 30 and 30's prev is 10
        self.assertEqual(dll.root.get_next().get_data(), 30)
        self.assertEqual(dll.end.get_prev().get_data(), 10)
        
        # Delete the first node (10)
        self.assertTrue(dll.delete(10))
        self.assertEqual(dll.to_list(), [30])
        self.assertEqual(dll.root, dll.end)
        self.assertIsNone(dll.root.get_prev())
        self.assertIsNone(dll.root.get_next())
        
        # Delete the last node (30)
        self.assertTrue(dll.delete(30))
        self.assertEqual(dll.to_list(), [])
        self.assertIsNone(dll.root)
        self.assertIsNone(dll.end)
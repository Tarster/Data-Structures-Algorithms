import unittest
from circular_linked_list import CircularLinkedList

# Circular Linked List Test
class CircularLinkedListTest(unittest.TestCase):
    # Test Case: Adding elements to the front
    def test_add_front(self):
        cll = CircularLinkedList()
        cll.add(10, pos="front")
        self.assertEqual(cll.to_list(), [10])
        cll.add(20, pos="front")
        self.assertEqual(cll.to_list(), [20, 10])
        cll.add(30, pos="front")
        self.assertEqual(cll.to_list(), [30, 20, 10])

    # Test Case: Adding elements to the end
    def test_add_end(self):
        cll = CircularLinkedList()
        cll.add(10, pos="end")
        self.assertEqual(cll.to_list(), [10])
        cll.add(20, pos="end")
        self.assertEqual(cll.to_list(), [10, 20])
        cll.add(30, pos="end")
        self.assertEqual(cll.to_list(), [10, 20, 30])

    # Test Case: Adding elements to front and end
    def test_add_front_end(self):
        cll = CircularLinkedList()
        cll.add(10, pos="front")
        cll.add(20, pos="end")
        cll.add(30, pos="front")
        cll.add(40, pos="end")
        self.assertEqual(cll.to_list(), [30, 10, 20, 40])

    # Test Case: Deleting elements from the list
    def test_delete(self):
        cll = CircularLinkedList()
        # Attempt to delete from empty list
        self.assertFalse(cll.delete(10))

        # Add elements
        cll.add(10, pos="front")
        cll.add(20, pos="end")
        cll.add(30, pos="front")
        cll.add(40, pos="end")  # List: [30, 10, 20, 40]
        self.assertEqual(cll.to_list(), [30, 10, 20, 40])

        # Delete front element
        self.assertTrue(cll.delete(30))
        self.assertEqual(cll.to_list(), [10, 20, 40])

        # Delete end element
        self.assertTrue(cll.delete(40))
        self.assertEqual(cll.to_list(), [10, 20])

        # Delete middle element
        self.assertTrue(cll.delete(20))
        self.assertEqual(cll.to_list(), [10])

        # Delete the only remaining element
        self.assertTrue(cll.delete(10))
        self.assertEqual(cll.to_list(), [])

        # Attempt to delete non-existent element
        self.assertFalse(cll.delete(50))

    # Test Case: Deleting elements with duplicates
    def test_delete_duplicates(self):
        cll = CircularLinkedList()
        cll.add(10, pos="front")
        cll.add(20, pos="end")
        cll.add(10, pos="end")
        cll.add(30, pos="front")  # List: [30, 10, 20, 10]
        self.assertEqual(cll.to_list(), [30, 10, 20, 10])

        # Delete first occurrence of 10
        self.assertTrue(cll.delete(10))
        self.assertEqual(cll.to_list(), [30, 20, 10])

        # Delete second occurrence of 10
        self.assertTrue(cll.delete(10))
        self.assertEqual(cll.to_list(), [30, 20])

        # Attempt to delete 10 again (no more 10s)
        self.assertFalse(cll.delete(10))
        self.assertEqual(cll.to_list(), [30, 20])

    # Test Case: Finding elements in the list
    def test_find(self):
        cll = CircularLinkedList()
        # Find in empty list
        self.assertFalse(cll.find(10))

        # Add elements
        cll.add(10, pos="front")
        cll.add(20, pos="end")
        cll.add(30, pos="front")
        cll.add(40, pos="end")  # List: [30, 10, 20, 40]

        # Find existing elements
        self.assertTrue(cll.find(30))
        self.assertTrue(cll.find(10))
        self.assertTrue(cll.find(20))
        self.assertTrue(cll.find(40))

        # Find non-existent element
        self.assertFalse(cll.find(50))

    # Test Case: Edge cases and boundary conditions
    def test_edge_cases(self):
        cll = CircularLinkedList()

        # Edge case: Adding and deleting a single element
        cll.add(100, pos="front")
        self.assertEqual(cll.to_list(), [100])
        self.assertTrue(cll.delete(100))
        self.assertEqual(cll.to_list(), [])

        # Edge case: Deleting from empty list
        self.assertFalse(cll.delete(200))

        # Edge case: Adding multiple elements and deleting all
        cll.add(10, pos="front")
        cll.add(20, pos="end")
        cll.add(30, pos="front")
        cll.add(40, pos="end")  # List: [30, 10, 20, 40]
        self.assertEqual(cll.to_list(), [30, 10, 20, 40])

        self.assertTrue(cll.delete(30))
        self.assertTrue(cll.delete(10))
        self.assertTrue(cll.delete(20))
        self.assertTrue(cll.delete(40))
        self.assertEqual(cll.to_list(), [])

    # Test Case: Converting to list
    def test_to_list(self):
        cll = CircularLinkedList()
        # Empty list
        self.assertEqual(cll.to_list(), [])

        # Add elements
        cll.add(1, pos="front")
        cll.add(2, pos="end")
        cll.add(3, pos="front")
        cll.add(4, pos="end")  # List: [3, 1, 2, 4]
        self.assertEqual(cll.to_list(), [3, 1, 2, 4])

        # Delete an element and check list
        cll.delete(1)  # List should be [3, 2, 4]
        self.assertEqual(cll.to_list(), [3, 2, 4])

    # Test Case: Ensuring circularity
    def test_circularity(self):
        cll = CircularLinkedList()
        cll.add(10, pos="front")
        cll.add(20, pos="end")
        cll.add(30, pos="front")  # List: [30, 10, 20]

        # The end node should point to the first node
        first_node = cll.end.get_next()
        self.assertEqual(first_node.get_data(), 30)
        self.assertEqual(cll.end.get_next().get_data(), 30)
        self.assertEqual(cll.end.get_next().get_next().get_data(), 10)
        self.assertEqual(cll.end.get_next().get_next().get_next().get_data(), 20)
        self.assertEqual(cll.end.get_next().get_next().get_next().get_next().get_data(), 30)


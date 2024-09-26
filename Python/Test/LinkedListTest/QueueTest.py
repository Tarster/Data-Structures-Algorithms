import unittest
import sys
sys.path.append(r'Python\Queue')

from Queue import Queue

class QueueTest(unittest.TestCase):
    def setUp(self):
        """Initialize a new Queue before each test."""
        self.queue = Queue()

    def test_initial_state(self):
        """Test that a new queue is empty."""
        self.assertTrue(self.queue.is_empty(), "New queue should be empty.")
        self.assertEqual(self.queue.size, 0, "Initial size should be 0.")
        self.assertIsNone(self.queue.get_front(), "Front of empty queue should be None.")
        self.assertIsNone(self.queue.get_rear(), "Rear of empty queue should be None.")
        self.assertEqual(self.queue.to_list(), [], "to_list of empty queue should be empty list.")

    def test_enqueue_single_element(self):
        """Test enqueueing a single element."""
        self.queue.enqueue(10)
        self.assertFalse(self.queue.is_empty(), "Queue should not be empty after enqueue.")
        self.assertEqual(self.queue.size, 1, "Size should be 1 after one enqueue.")
        self.assertEqual(self.queue.get_front(), 10, "Front should be the enqueued element.")
        self.assertEqual(self.queue.get_rear(), 10, "Rear should be the enqueued element.")
        self.assertEqual(self.queue.to_list(), [10], "to_list should return list with one element.")

    def test_enqueue_multiple_elements(self):
        """Test enqueueing multiple elements."""
        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            self.queue.enqueue(elem)
        self.assertFalse(self.queue.is_empty(), "Queue should not be empty after enqueueing elements.")
        self.assertEqual(self.queue.size, len(elements), f"Size should be {len(elements)} after enqueueing.")
        self.assertEqual(self.queue.get_front(), elements[0], "Front should be the first enqueued element.")
        self.assertEqual(self.queue.get_rear(), elements[-1], "Rear should be the last enqueued element.")
        self.assertEqual(self.queue.to_list(), elements, "to_list should return all enqueued elements in order.")

    def test_dequeue_single_element(self):
        """Test dequeueing a single element."""
        self.queue.enqueue(100)
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued, 100, "Dequeued element should be the enqueued element.")
        self.assertTrue(self.queue.is_empty(), "Queue should be empty after dequeueing the only element.")
        self.assertEqual(self.queue.size, 0, "Size should be 0 after dequeueing the only element.")
        self.assertIsNone(self.queue.get_front(), "Front should be None after dequeueing all elements.")
        self.assertIsNone(self.queue.get_rear(), "Rear should be None after dequeueing all elements.")
        self.assertEqual(self.queue.to_list(), [], "to_list should be empty after dequeueing all elements.")

    def test_dequeue_multiple_elements(self):
        """Test dequeueing multiple elements."""
        elements = [10, 20, 30, 40, 50]
        for elem in elements:
            self.queue.enqueue(elem)
        for i, elem in enumerate(elements):
            dequeued = self.queue.dequeue()
            self.assertEqual(dequeued, elem, f"Dequeued element should be {elem}.")
            expected_size = len(elements) - (i + 1)
            self.assertEqual(self.queue.size, expected_size, f"Size should be {expected_size} after dequeueing.")
            if expected_size > 0:
                self.assertEqual(self.queue.get_front(), elements[i + 1], "Front should update correctly after dequeue.")
            else:
                self.assertIsNone(self.queue.get_front(), "Front should be None when queue is empty.")
        self.assertTrue(self.queue.is_empty(), "Queue should be empty after dequeueing all elements.")
        self.assertEqual(self.queue.to_list(), [], "to_list should be empty after dequeueing all elements.")

    def test_dequeue_from_empty_queue(self):
        """Test dequeueing from an empty queue."""
        dequeued = self.queue.dequeue()
        self.assertIsNone(dequeued, "Dequeueing from empty queue should return None.")
        self.assertTrue(self.queue.is_empty(), "Queue should remain empty after dequeueing from empty queue.")
        self.assertEqual(self.queue.size, 0, "Size should remain 0 after dequeueing from empty queue.")

    def test_mixed_operations(self):
        """Test a mix of enqueue and dequeue operations."""
        self.queue.enqueue(1)
        self.queue.enqueue(2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.to_list(), [1, 2, 3], "Queue should contain [1, 2, 3].")
        
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued, 1, "First dequeued element should be 1.")
        self.assertEqual(self.queue.to_list(), [2, 3], "Queue should contain [2, 3] after one dequeue.")
        
        self.queue.enqueue(4)
        self.assertEqual(self.queue.to_list(), [2, 3, 4], "Queue should contain [2, 3, 4].")
        
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued, 2, "Second dequeued element should be 2.")
        self.assertEqual(self.queue.to_list(), [3, 4], "Queue should contain [3, 4] after two dequeues.")
        
        self.queue.enqueue(5)
        self.assertEqual(self.queue.to_list(), [3, 4, 5], "Queue should contain [3, 4, 5].")
        
        while not self.queue.is_empty():
            self.queue.dequeue()
        self.assertTrue(self.queue.is_empty(), "Queue should be empty after dequeuing all elements.")
        self.assertEqual(self.queue.to_list(), [], "to_list should be empty after dequeuing all elements.")

    def test_get_front_and_rear(self):
        """Test get_front and get_rear methods."""
        self.assertIsNone(self.queue.get_front(), "get_front should return None for empty queue.")
        self.assertIsNone(self.queue.get_rear(), "get_rear should return None for empty queue.")
        
        self.queue.enqueue('a')
        self.assertEqual(self.queue.get_front(), 'a', "get_front should return 'a'.")
        self.assertEqual(self.queue.get_rear(), 'a', "get_rear should return 'a'.")
        
        self.queue.enqueue('b')
        self.assertEqual(self.queue.get_front(), 'a', "get_front should still return 'a'.")
        self.assertEqual(self.queue.get_rear(), 'b', "get_rear should return 'b'.")
        
        self.queue.enqueue('c')
        self.assertEqual(self.queue.get_front(), 'a', "get_front should still return 'a'.")
        self.assertEqual(self.queue.get_rear(), 'c', "get_rear should return 'c'.")
        
        self.queue.dequeue()
        self.assertEqual(self.queue.get_front(), 'b', "After dequeue, get_front should return 'b'.")
        self.assertEqual(self.queue.get_rear(), 'c', "get_rear should still return 'c'.")
        
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertIsNone(self.queue.get_front(), "After dequeuing all elements, get_front should return None.")
        self.assertIsNone(self.queue.get_rear(), "After dequeuing all elements, get_rear should return None.")

    def test_to_list(self):
        """Test the to_list method."""
        self.assertEqual(self.queue.to_list(), [], "to_list should return empty list for empty queue.")
        
        elements = ['first', 'second', 'third']
        for elem in elements:
            self.queue.enqueue(elem)
        self.assertEqual(self.queue.to_list(), elements, "to_list should return all enqueued elements in order.")
        
        self.queue.dequeue()
        expected = elements[1:]
        self.assertEqual(self.queue.to_list(), expected, "to_list should reflect dequeued elements.")
        
        self.queue.enqueue('fourth')
        expected.append('fourth')
        self.assertEqual(self.queue.to_list(), expected, "to_list should include newly enqueued elements.")

    def test_size_property(self):
        """Test that the size property accurately reflects the number of elements."""
        self.assertEqual(self.queue.size, 0, "Initial size should be 0.")
        
        self.queue.enqueue(1)
        self.assertEqual(self.queue.size, 1, "Size should be 1 after one enqueue.")
        
        self.queue.enqueue(2)
        self.assertEqual(self.queue.size, 2, "Size should be 2 after two enqueues.")
        
        self.queue.dequeue()
        self.assertEqual(self.queue.size, 1, "Size should be 1 after one dequeue.")
        
        self.queue.dequeue()
        self.assertEqual(self.queue.size, 0, "Size should be 0 after dequeuing all elements.")
        
        self.queue.dequeue()  # Dequeue from empty
        self.assertEqual(self.queue.size, 0, "Size should remain 0 after dequeuing from empty queue.")

    def test_enqueue_after_dequeue_to_empty(self):
        """Test enqueueing after dequeuing all elements to ensure the queue resets correctly."""
        self.queue.enqueue(10)
        self.queue.enqueue(20)
        self.queue.dequeue()
        self.queue.dequeue()
        self.assertTrue(self.queue.is_empty(), "Queue should be empty after dequeuing all elements.")
        
        self.queue.enqueue(30)
        self.assertFalse(self.queue.is_empty(), "Queue should not be empty after enqueueing new element.")
        self.assertEqual(self.queue.get_front(), 30, "Front should be the newly enqueued element.")
        self.assertEqual(self.queue.get_rear(), 30, "Rear should be the newly enqueued element.")
        self.assertEqual(self.queue.to_list(), [30], "to_list should contain the newly enqueued element.")

    def test_enqueue_dequeue_interleaved(self):
        """Test enqueue and dequeue operations interleaved in various orders."""
        self.queue.enqueue(1)
        self.assertEqual(self.queue.get_front(), 1)
        self.queue.enqueue(2)
        self.assertEqual(self.queue.get_rear(), 2)
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued, 1)
        self.assertEqual(self.queue.get_front(), 2)
        self.queue.enqueue(3)
        self.assertEqual(self.queue.get_rear(), 3)
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued, 2)
        self.assertEqual(self.queue.get_front(), 3)
        dequeued = self.queue.dequeue()
        self.assertEqual(dequeued, 3)
        self.assertTrue(self.queue.is_empty())

    def test_enqueue_none(self):
        """Test enqueueing None as a valid element."""
        self.queue.enqueue(None)
        self.assertFalse(self.queue.is_empty(), "Queue should not be empty after enqueueing None.")
        self.assertEqual(self.queue.get_front(), None, "Front should be None after enqueueing None.")
        self.assertEqual(self.queue.get_rear(), None, "Rear should be None after enqueueing None.")
        self.assertEqual(self.queue.to_list(), [None], "to_list should contain [None].")
        dequeued = self.queue.dequeue()
        self.assertIsNone(dequeued, "Dequeued element should be None.")
        self.assertTrue(self.queue.is_empty(), "Queue should be empty after dequeuing None.")

    def test_enqueue_various_data_types(self):
        """Test enqueueing elements of various data types."""
        elements = [123, "string", 45.67, {'key': 'value'}, [1, 2, 3], (4, 5), None]
        for elem in elements:
            self.queue.enqueue(elem)
        self.assertEqual(self.queue.to_list(), elements, "to_list should contain all enqueued elements of various types.")
        for elem in elements:
            dequeued = self.queue.dequeue()
            self.assertEqual(dequeued, elem, f"Dequeued element should be {elem}.")
        self.assertTrue(self.queue.is_empty(), "Queue should be empty after dequeuing all elements.")

    def test_large_number_of_elements(self):
        """Test enqueueing and dequeueing a large number of elements."""
        large_number = 1000
        for i in range(large_number):
            self.queue.enqueue(i)
        self.assertEqual(self.queue.size, large_number, f"Size should be {large_number} after enqueueing.")
        for i in range(large_number):
            dequeued = self.queue.dequeue()
            self.assertEqual(dequeued, i, f"Dequeued element should be {i}.")
        self.assertTrue(self.queue.is_empty(), "Queue should be empty after dequeuing all elements.")
        self.assertEqual(self.queue.size, 0, "Size should be 0 after dequeuing all elements.")

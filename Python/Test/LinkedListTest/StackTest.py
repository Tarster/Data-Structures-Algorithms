import unittest
import sys
sys.path.append(r'Python\Stack')

from simple_stack import SimpleStack


class SimpleStackTest(unittest.TestCase):
    # Test Case: Initializing the stack
    def test_initialization(self):
        stack = SimpleStack()
        self.assertTrue(stack.isEmpty())
        self.assertEqual(stack.get_size(), 0)
        self.assertIsNone(stack.get_top())
        self.assertEqual(stack.to_list(), [])

    # Test Case: Pushing elements onto the stack
    def test_push(self):
        stack = SimpleStack()
        stack.push(10)
        self.assertFalse(stack.isEmpty())
        self.assertEqual(stack.get_size(), 1)
        self.assertEqual(stack.get_top(), 10)
        self.assertEqual(stack.to_list(), [10])
        
        stack.push(20)
        self.assertEqual(stack.get_size(), 2)
        self.assertEqual(stack.get_top(), 20)
        self.assertEqual(stack.to_list(), [20, 10])
        
        stack.push(30)
        self.assertEqual(stack.get_size(), 3)
        self.assertEqual(stack.get_top(), 30)
        self.assertEqual(stack.to_list(), [30, 20, 10])

    # Test Case: Popping elements from the stack
    def test_pop(self):
        stack = SimpleStack()
        
        # Pop from empty stack
        self.assertIsNone(stack.pop())
        self.assertTrue(stack.isEmpty())
        self.assertEqual(stack.get_size(), 0)
        
        # Push elements and pop them
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.get_size(), 3)
        self.assertEqual(stack.to_list(), [30, 20, 10])
        
        popped = stack.pop()
        self.assertEqual(popped, 30)
        self.assertEqual(stack.get_size(), 2)
        self.assertEqual(stack.to_list(), [20, 10])
        
        popped = stack.pop()
        self.assertEqual(popped, 20)
        self.assertEqual(stack.get_size(), 1)
        self.assertEqual(stack.to_list(), [10])
        
        popped = stack.pop()
        self.assertEqual(popped, 10)
        self.assertEqual(stack.get_size(), 0)
        self.assertTrue(stack.isEmpty())
        self.assertEqual(stack.to_list(), [])
        
        # Pop again from empty stack
        self.assertIsNone(stack.pop())

    # Test Case: Getting the top element without popping
    def test_get_top(self):
        stack = SimpleStack()
        
        # Top of empty stack
        self.assertIsNone(stack.get_top())
        
        # Push elements and get top
        stack.push(10)
        self.assertEqual(stack.get_top(), 10)
        
        stack.push(20)
        self.assertEqual(stack.get_top(), 20)
        
        stack.push(30)
        self.assertEqual(stack.get_top(), 30)
        
        # Pop and check top
        stack.pop()
        self.assertEqual(stack.get_top(), 20)
        
        stack.pop()
        self.assertEqual(stack.get_top(), 10)
        
        stack.pop()
        self.assertIsNone(stack.get_top())

    # Test Case: Checking if the stack is empty
    def test_is_empty(self):
        stack = SimpleStack()
        self.assertTrue(stack.isEmpty())
        
        stack.push(10)
        self.assertFalse(stack.isEmpty())
        
        stack.pop()
        self.assertTrue(stack.isEmpty())

    # Test Case: Checking the size of the stack
    def test_size(self):
        stack = SimpleStack()
        self.assertEqual(stack.get_size(), 0)
        
        stack.push(10)
        self.assertEqual(stack.get_size(), 1)
        
        stack.push(20)
        self.assertEqual(stack.get_size(), 2)
        
        stack.pop()
        self.assertEqual(stack.get_size(), 1)
        
        stack.pop()
        self.assertEqual(stack.get_size(), 0)

    # Test Case: Pushing and popping multiple elements
    def test_multiple_push_pop(self):
        stack = SimpleStack()
        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            stack.push(elem)
            self.assertEqual(stack.get_top(), elem)
            self.assertEqual(stack.get_size(), elements.index(elem)+1)
        
        for elem in reversed(elements):
            self.assertEqual(stack.get_top(), elem)
            popped = stack.pop()
            self.assertEqual(popped, elem)
            self.assertEqual(stack.get_size(), elements.index(elem))
        
        self.assertTrue(stack.isEmpty())

    # Test Case: Pushing None as data
    def test_push_none(self):
        stack = SimpleStack()
        stack.push(None)
        self.assertFalse(stack.isEmpty())
        self.assertEqual(stack.get_size(), 1)
        self.assertIsNone(stack.get_top())
        self.assertEqual(stack.to_list(), [None])
        
        stack.push(10)
        self.assertEqual(stack.get_top(), 10)
        self.assertEqual(stack.to_list(), [10, None])
        
        popped = stack.pop()
        self.assertEqual(popped, 10)
        self.assertEqual(stack.get_top(), None)
        self.assertEqual(stack.to_list(), [None])
        
        popped = stack.pop()
        self.assertIsNone(popped)
        self.assertTrue(stack.isEmpty())

    # Test Case: Pushing duplicate elements
    def test_push_duplicates(self):
        stack = SimpleStack()
        stack.push(10)
        stack.push(10)
        stack.push(10)
        self.assertEqual(stack.get_size(), 3)
        self.assertEqual(stack.to_list(), [10, 10, 10])
        
        popped = stack.pop()
        self.assertEqual(popped, 10)
        self.assertEqual(stack.get_size(), 2)
        self.assertEqual(stack.to_list(), [10, 10])
        
        popped = stack.pop()
        self.assertEqual(popped, 10)
        self.assertEqual(stack.get_size(), 1)
        self.assertEqual(stack.to_list(), [10])
        
        popped = stack.pop()
        self.assertEqual(popped, 10)
        self.assertTrue(stack.isEmpty())
        self.assertEqual(stack.to_list(), [])

    # Test Case: Ensuring no data corruption after multiple operations
    def test_data_integrity(self):
        stack = SimpleStack()
        operations = [
            ('push', 10),
            ('push', 20),
            ('push', 30),
            ('pop', 30),
            ('push', 40),
            ('pop', 40),
            ('pop', 20),
            ('push', 50),
            ('pop', 50),
            ('pop', 10),
        ]
        expected_sizes = [1, 2, 3, 2, 3, 2, 1, 2, 1, 0]
        expected_tops = [10, 20, 30, 20, 40, 20, 10, 50, 10, None]
        expected_lists = [
            [10],
            [20, 10],
            [30, 20, 10],
            [20, 10],
            [40, 20, 10],
            [20, 10],
            [10],
            [50, 10],
            [10],
            []
        ]
        
        for i, (op, value) in enumerate(operations):
            if op == 'push':
                stack.push(value)
                self.assertEqual(stack.get_size(), expected_sizes[i])
                self.assertEqual(stack.get_top(), expected_tops[i])
                self.assertEqual(stack.to_list(), expected_lists[i])
            elif op == 'pop':
                popped = stack.pop()
                self.assertEqual(popped, value)
                self.assertEqual(stack.get_size(), expected_sizes[i])
                self.assertEqual(stack.get_top(), expected_tops[i])
                self.assertEqual(stack.to_list(), expected_lists[i])

    # Test Case: Converting stack to list
    def test_to_list(self):
        stack = SimpleStack()
        # Empty stack
        self.assertEqual(stack.to_list(), [])
        
        # Push elements
        stack.push(10)
        stack.push(20)
        stack.push(30)  # Stack: [30, 20, 10]
        self.assertEqual(stack.to_list(), [30, 20, 10])
        
        # Pop an element and check list
        stack.pop()  # Stack: [20, 10]
        self.assertEqual(stack.to_list(), [20, 10])
        
        # Push another element
        stack.push(40)  # Stack: [40, 20, 10]
        self.assertEqual(stack.to_list(), [40, 20, 10])
        
        # Pop all elements
        stack.pop()  # Stack: [20, 10]
        stack.pop()  # Stack: [10]
        stack.pop()  # Stack: []
        self.assertEqual(stack.to_list(), [])
    
    # Test Case: Ensuring stack behaves correctly under stress (large number of operations)
    def test_stress(self):
        stack = SimpleStack()
        num_operations = 1000
        for i in range(num_operations):
            stack.push(i)
            self.assertEqual(stack.get_size(), i+1)
            self.assertEqual(stack.get_top(), i)
        
        for i in reversed(range(num_operations)):
            self.assertEqual(stack.get_top(), i)
            popped = stack.pop()
            self.assertEqual(popped, i)
            self.assertEqual(stack.get_size(), i)
        
        self.assertTrue(stack.isEmpty())
        self.assertEqual(stack.to_list(), [])

    # Test Case: Ensuring stack handles mixed data types
    def test_mixed_data_types(self):
        stack = SimpleStack()
        mixed_data = [10, "twenty", 30.5, None, [40], {"fifty": 50}]
        for item in mixed_data:
            stack.push(item)
        
        self.assertEqual(stack.get_size(), len(mixed_data))
        self.assertEqual(stack.get_top(), {"fifty": 50})
        self.assertEqual(stack.to_list(), [{"fifty": 50}, [40], None, 30.5, "twenty", 10])
        
        # Pop all elements and check
        for item in reversed(mixed_data):
            popped = stack.pop()
            self.assertEqual(popped, item)
        
        self.assertTrue(stack.isEmpty())
        self.assertEqual(stack.to_list(), [])

    # Test Case: Ensuring stack does not allow external modification of nodes
    def test_encapsulation(self):
        stack = SimpleStack()
        stack.push(10)
        stack.push(20)
        
        # Attempt to modify the node externally
        first_node = stack.top
        first_node.set_data(100)
        self.assertEqual(stack.get_top(), 100)
        self.assertEqual(stack.to_list(), [100, 10])
        
        # Attempt to change the next pointer externally
        second_node = first_node.get_next()
        second_node.set_next(None)
        self.assertEqual(stack.get_size(), 2)
        self.assertEqual(stack.to_list(), [100, 10])
        # Popping should still work correctly
        popped = stack.pop()
        self.assertEqual(popped, 100)
        self.assertEqual(stack.to_list(), [10])
        popped = stack.pop()
        self.assertEqual(popped, 10)
        self.assertEqual(stack.to_list(), [])

    # Test Case: Ensuring stack maintains correct order (LIFO)
    def test_order(self):
        stack = SimpleStack()
        elements = [1, 2, 3, 4, 5]
        for elem in elements:
            stack.push(elem)
        
        expected_order = list(reversed(elements))  # [5,4,3,2,1]
        self.assertEqual(stack.to_list(), expected_order)
        
        for elem in expected_order:
            popped = stack.pop()
            self.assertEqual(popped, elem)
        
        self.assertTrue(stack.isEmpty())

if __name__ == '__main__':
    unittest.main()

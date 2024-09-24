# Singly Linked List Implementation
import sys

# Add the path to the sys.path
sys.path.append(r'Python\BaseClass')

from base_class import Node

class SimpleStack():

    def __init__(self):
        self.top = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    # Get the size of the LinkedList
    def get_size(self):
        return self.size
    
    # Add to the linked list
    def push(self, data):
        new_node = Node(data)
        # Adding the first element to the stack
        if self.top is None:
            self.top = new_node
        else:
            # Point the new node to the existing top node
            new_node.set_next(self.top)
            # Update the top to the new node
            self.top = new_node
        self.size += 1

    # Return the top data element from the stack
    def get_top(self):
        if self.top == None:
            return
        else:
            return self.top.get_data()
    
    # Remove the element from the top:
    def pop(self):
        # If stack is empty
        if self.top is None:
            return None  # Or consider raising an exception
        # If it has elements
        else:
            popped_node = self.top
            self.top = self.top.get_next()
            self.size -= 1
            return popped_node.get_data()

    def print_list(self):
        this_node = self.top
        while this_node:
            print(this_node.get_data(),"-> ", end="")
            this_node = this_node.get_next()

    
    def to_list(self):
        result = []
        current = self.top
        while current is not None:
            result.append(current.data)
            current = current.next
        return result
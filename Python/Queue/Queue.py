# Singly Linked List Implementation
import sys

# Add the path to the sys.path
sys.path.append(r'Python\BaseClass')

from base_class import Node

class Queue(object):
    def __init__(self) -> None:
        self.head = None
        self.rear = None
        self.size = 0

    
    def enqueue(self, data):
        new_node = Node(data)

        # if there is no node in the structure
        if self.size == 0:
            self.head = new_node
            self.rear = new_node
        else:
            self.rear.set_next(new_node)
            self.rear = new_node

        self.size += 1
    
    def dequeue(self):
        if self.size == 0:
            return None
        elif self.size == 1:
            deleted_node = self.head.get_data()
            self.head = None
            self.rear = None
        else:
            deleted_node = self.head.get_data()
            self.head = self.head.get_next()
        
        self.size -= 1
        return deleted_node
    
    def is_empty(self):
        return self.size == 0

    def get_front(self):
        if self.head == None:
            return None
        return self.head.get_data()

    def get_rear(self):
        if self.rear == None:
            return None
        return self.rear.get_data()
    
    def to_list(self):
        result = []
        current = self.head
        while current is not None:
            result.append(current.data)
            current = current.get_next()
        return result
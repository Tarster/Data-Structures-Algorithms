# Base Class for LinkedList
class Node(object):
    
    def __init__(self, data, next_node = None):
        self.data = data
        self.next = next_node
    
    # Getters
    def get_next(self):
        return self.next
    def get_data(self):
        return self.data
    
    # Setters
    def set_next(self,next_node = None):
        self.next = next_node
    def set_data(self, data = None):
        self.data = data

class DoubleNode(Node):
    # Overloaded constructor
    def __init__(self, data, next_node = None, prev_node = None):
        Node.__init__(self, data, next_node)
        self.prev = prev_node
    
    # Additional Getter and Setters
    def get_prev(self):
        return self.prev
    
    def set_prev(self, prev_node = None):
        self.prev = prev_node
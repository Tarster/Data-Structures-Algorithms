
# Singly Linked List Implementation
import sys

# Add the path to the sys.path
sys.path.append(r'Python\BaseClass')

from base_class import Node

class LinkedList():
    def __init__(self):
        self.root = None
        self.size = 0

    # Get the size of the LinkedList
    def get_size(self):
        return self.size
    
    # Add to the linked list
    def add(self, data):
        new_node = Node(data, self.root)
        self.root = new_node
        self.size += 1

    def remove(self, data):
        this_node = self.root
        prev_node = None
        
        while this_node:
            if this_node.get_data() == data:
                if prev_node:
                    # Get the information which node current node is pointing to and set it as the next node
                    prev_node.set_next(this_node.get_next())
                else:
                    self.root = this_node
                self.size -= 1
                return True
            else:
                prev_node = this_node
                this_node = this_node.get_next()
        # The value is not found hence not removed
        return False

    def find(self, data):
        this_node = self.root
        # Continue looking for it
        while this_node:
            # If not found just return None else return data
            if this_node.get_data() == data:
                return True
            else:
                this_node = this_node.get_next()
        return False
    
    def print_list(self):
        this_node = self.root
        while this_node:
            print(this_node.get_data(),"-> ", end="")
            this_node = this_node.get_next()
        print("None")



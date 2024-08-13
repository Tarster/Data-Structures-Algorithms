import sys
# Add path to the file
sys.path.append(r'Python\BaseClass')

from base_class import DoubleNode

class DoubleLinkedList(object):

    def __init__(self) -> None:
        self.root = None
        self.end = None
        self.size = 0
    
    def add(self, data=None, place = "back"):
        new_node = DoubleNode(data)
        if self.size == 0:
            self.root = new_node
            self.end = new_node
        
        elif place == "back": 
            last_node = self.end
            # Set the last node previous
            last_node.set_next(new_node)
            # Set both the link for new node
            new_node.set_prev(last_node)
            self.end = new_node
        else:
            first_node = self.root
            first_node.set_prev(new_node)
            new_node.set_next(first_node) 
            self.root = new_node
        self.size += 1

    def delete(self, data=None):
        this_node = self.root
        while this_node:
            # If we find the data
            if this_node.get_data() == data:
                if self.size == 1:
                    self.root = None
                    self.end = None
                # find if it's a root node
                elif this_node == self.root:
                    # Set root to next node
                    self.root = this_node.get_next()
                    # Set previous of next_node to None
                    next_node = self.root
                    next_node.set_prev()
                
                elif this_node == self.end:
                    # get the last node
                    last_node = this_node.get_prev()
                    # set the last node next to None
                    last_node.set_next()
                    # set the end to previous node
                    self.end = last_node
                else:
                    # Get the previous node and next node
                    prev_node = this_node.get_prev()
                    next_node = this_node.get_next()
                    # The previous node's next will point to the next node
                    prev_node.set_next(next_node)
                    # The next node's previous will be pointing towards the previous node
                    next_node.set_prev(prev_node)
                self.size -= 1
                return True
            
            this_node = this_node.get_next()        
        return False 

    def find(self, data=None):
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return True
            this_node = this_node.get_next()
        return False
    
    def printDoubleList(self, place = "front"):
        if place == "front":
            print("Printing from Front:")
            this_node = self.root
            while this_node:
                print(this_node.data,"-> ", end="")
                this_node = this_node.get_next()
            print("None")
        
        else:
            print("Printing from End:")
            this_node = self.end
            while this_node:
                print(this_node.data, "-> ", end="")
                this_node = this_node.get_prev()
            print("None")
            

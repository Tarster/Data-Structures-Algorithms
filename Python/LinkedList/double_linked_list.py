import sys
# Add path to the file
sys.path.append(r'Python\BaseClass')

from base_class import DoubleNode


class DoubleLinkedList(object):

    def __init__(self) -> None:
        self.root = None
        self.end = None
        self.size = 0
    
    def add(self, data=None, place="back"):
        new_node = DoubleNode(data)
        if self.size == 0:
            # First node in the list
            self.root = new_node
            self.end = new_node
        elif place == "back":
            # Add to the end
            last_node = self.end
            last_node.set_next(new_node)
            new_node.set_prev(last_node)
            self.end = new_node
        elif place == "front":
            # Add to the front
            first_node = self.root
            first_node.set_prev(new_node)
            new_node.set_next(first_node)
            self.root = new_node
        else:
            raise ValueError("Invalid position specified. Use 'front' or 'back'.")
        self.size += 1

    def delete(self, data=None):
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                if self.size == 1:
                    # Only one node in the list
                    self.root = None
                    self.end = None
                elif this_node == self.root:
                    # Deleting the root node
                    self.root = this_node.get_next()
                    if self.root:
                        self.root.set_prev(None)
                elif this_node == self.end:
                    # Deleting the end node
                    self.end = this_node.get_prev()
                    if self.end:
                        self.end.set_next(None)
                else:
                    # Deleting a middle node
                    prev_node = this_node.get_prev()
                    next_node = this_node.get_next()
                    if prev_node:
                        prev_node.set_next(next_node)
                    if next_node:
                        next_node.set_prev(prev_node)
                self.size -= 1
                return True
            this_node = this_node.get_next()
        return False  # Data not found 

    def find(self, data=None):
        this_node = self.root
        while this_node:
            if this_node.get_data() == data:
                return True
            this_node = this_node.get_next()
        return False
    
    def printDoubleList(self, place="front"):
        if place == "front":
            print("Printing from Front:")
            this_node = self.root
            while this_node:
                print(this_node.data, "-> ", end="")
                this_node = this_node.get_next()
            print("None")
        elif place == "end":
            print("Printing from End:")
            this_node = self.end
            while this_node:
                print(this_node.data, "-> ", end="")
                this_node = this_node.get_prev()
            print("None")
        else:
            raise ValueError("Invalid print direction. Use 'front' or 'end'.")
    
    def to_list(self):
        result = []
        current = self.root
        while current is not None:
            result.append(current.data)
            current = current.get_next()
        return result
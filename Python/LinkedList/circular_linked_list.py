import sys
sys.path.append("Python/BaseClass")
from base_class import Node

class CircularLinkedList(object):
    def __init__(self) -> None:
        self.end = None
        self.size = 0

    def add(self, data, pos = "front"):
        new_node = Node(data)
        if self.size == 0:
            # Set the root
            self.end = new_node
            # Set the current root to itself
            new_node.set_next(new_node)

        elif self.size > 0 and pos == "front":
            front_node  = self.end.get_next()
            # set the new node next to the current first node
            new_node.set_next(front_node)
            # set the end node next to current node
            self.end.set_next(new_node)
        else:
            # point new node to start
            new_node.set_next(self.end.get_next())
            # point end node to the new node 
            self.end.set_next(new_node)
            # move end pointer to the new node
            self.end = new_node
        self.size += 1

    def delete(self, data):
        if self.size == 0:
            return False
        curr_node = self.end.get_next()
        prev_node = self.end
        flag = True
        while curr_node != self.end.get_next() or flag:
            flag = False
            if curr_node.get_data() == data:
                if self.size == 1:
                    self.end = None
                else:
                    # last node in the list
                    if curr_node == self.end:
                        self.end = prev_node
                    # Set the previous node to the next of current node
                    prev_node.set_next(curr_node.get_next())       
                self.size -=1
                return True
            else:
                prev_node = curr_node
                curr_node = curr_node.get_next()
        return False
            
    def find(self, data):
        if self.size == 0:
            return False
        curr_node = self.end.get_next()
        flag = True
        while curr_node != self.end.get_next() or flag:
            flag = False
            if curr_node.get_data() == data:
                return True
            curr_node = curr_node.get_next()
        return False
        
    def print_list(self):
        if self.size == 0:
            print("None")
            return

        curr_node = self.end.get_next() # get the first element
        flag = True
        while curr_node != self.end.get_next() or flag: 
            flag = False
            print(curr_node.get_data(),"-> ",end="")
            curr_node = curr_node.get_next()
        print()
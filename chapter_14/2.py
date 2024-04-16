# Add a method to the DoublyLinkedList class that prints all the values of the list in reverse order.

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.previous_node = None

class DoublyLinkedList:
    def __init__(self, first_node=None, last_node=None):
        self.first_node = first_node
        self.last_node = last_node
    
    def append(self, value):
        new_node = Node(value)
        if not self.first_node:
            self.first_node = new_node
            self.last_node = new_node
        else:
            new_node.previous_node = self.last_node
            self.last_node.next_node = new_node
            self.last_node = new_node

    def pop_head(self):
        popped_node = self.first_node
        self.first_node = self.first_node.next_node
        self.first_node.previous_node = None
        return popped_node
    
    def print_all_in_reverse(self):
        current_node = self.last_node
        while current_node:
            print(current_node.data)
            current_node = current_node.previous_node

node_1 = Node("once")
node_2 = Node("upon")
node_3 = Node("a")
node_4 = Node("time")

node_1.next_node = node_2
node_2.next_node = node_3
node_3.next_node = node_4

node_2.previous_node = node_1
node_3.previous_node = node_2
node_4.previous_node = node_3

my_list = DoublyLinkedList(node_1, node_4)

my_list.print_all_in_reverse()
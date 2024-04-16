import doubly_linked_list

class Queue:
    def __init__(self):
        self.data = doubly_linked_list.DoublyLinkedList()
    
    def enqueue(self, element):
        self.data.append(element)
    
    def dequeue(self):
        dequeued_node = self.data.pop_head()
        return dequeued_node.data

    def read(self):
        if not self.data.first_node:
            return None
        return self.data.first_node.data
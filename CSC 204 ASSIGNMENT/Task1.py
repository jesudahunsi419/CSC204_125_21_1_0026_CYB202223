
from nodes.node import Node

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=' -> ')
            current = current.next
        print("None")

    def find_max_min(self):
        if not self.head:
            return None, None

        max_data = self.head.data
        min_data = self.head.data

        current = self.head.next
        while current:
            if current.data > max_data:
                max_data = current.data
            if current.data < min_data:
                min_data = current.data
            current = current.next

        return max_data, min_data

    def list_to_bst(self, lst):
        if not lst:
            return None

        mid = len(lst) // 2
        root = Node(lst[mid])

        root.left = self.list_to_bst(lst[:mid])
        root.right = self.list_to_bst(lst[mid + 1:])

        return root

#binary search algorithm on unsorted array

def binary_search_unsorted(self, key):
    current = self.head
    index = 0
    while current:
        if current.data == key:
            return index
        current = current.next
        index += 1
    return -1

#Queue data structure using structured linked list
class QueueUsingLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        self.front = self.front.next
        return data

    def display(self):
        current = self.front
        while current:
            print(current.data, end=' <- ')
            current = current.next
        print("None")
#Attempt to sort the Queue  
def sort_queue(self):
    elements = []
    while not self.is_empty():
        elements.append(self.dequeue())
    elements.sort()
    for element in elements:
        self.enqueue(element)
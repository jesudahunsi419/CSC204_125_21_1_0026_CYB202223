class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Other methods (e.g., append, insert, delete) can be added here

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def find_max(self):
        if self.head is None:
            return None
        current = self.head
        max_data = current.data
        while current:
            if current.data > max_data:
                max_data = current.data
            current = current.next
        return max_data

    def find_min(self):
        if self.head is None:
            return None
        current = self.head
        min_data = current.data
        while current:
            if current.data < min_data:
                min_data = current.data
            current = current.next
        return min_data


# Example usage:
if __name__ == "__main__":
    # Create a linked list
    linked_list = LinkedList()
    linked_list.head = Node(5)
    second_node = Node(3)
    third_node = Node(8)
    fourth_node = Node(1)
    fifth_node = Node(6)

    linked_list.head.next = second_node
    second_node.next = third_node
    third_node.next = fourth_node
    fourth_node.next = fifth_node

    # Display the linked list
    linked_list.display()

    # Find and display the maximum and minimum data
    max_data = linked_list.find_max()
    min_data = linked_list.find_min()
    print(f"\nMaximum data: {max_data}")
    print(f"Minimum data: {min_data}")
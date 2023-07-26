class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def sorted_list_to_bst(head):
    if not head:
        return None

    # Find the middle element using slow and fast pointers
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next

    # Create a TreeNode with the value of the middle element
    root = TreeNode(slow.value)

    # If there's only one element in the list, return the TreeNode
    if slow == fast:
        return root

    # Recursively convert left and right halves of the linked list into subtrees
    prev.next = None  # Split the list into two halves
    root.left = sorted_list_to_bst(head)
    root.right = sorted_list_to_bst(slow.next)

    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=" ")
        inorder_traversal(root.right)


if __name__ == "__main__":
    # Test with the given list [1,3,4,5,6,8,7,9,2,22,15,55,45,23,24,26,28]
    linked_list = ListNode(1)
    current = linked_list
    values = [3, 4, 5, 6, 8, 7, 9, 2, 22, 15, 55, 45, 23, 24, 26, 28]
    for value in values:
        current.next = ListNode(value)
        current = current.next

    print("Original Linked List:")
    current = linked_list
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

    # Convert the linked list to a binary search tree
    bst_root = sorted_list_to_bst(linked_list)

    print("\nBinary Search Tree (Inorder Traversal):")
    inorder_traversal(bst_root)
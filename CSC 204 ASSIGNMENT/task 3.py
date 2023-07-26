class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sorted_list_to_bst(head):
    ifnot head:
        returnNone
    
    #To find the middle node of a  linked list
    def find_middle(start, end):
        slow = start
        fast = start
        while fast != end and fast.next != end:
            slow = slow.next
            fast = fast.next.next
        return slow
        
    
    #Convert Singly Linked List to binary search tree
    def convert_to_bst(start, end):
        if start == end:
            returnNone
        
        mid = find_middle(start, end)
        node = TreeNode(mid.val)

        node.left = convert_to_bst(start, mid)
        node.right = convert_to_bst(mid.next, end)
        
        return node
    
    root = convert_to_bst(head, None)

    return root

#Function to print the in_order traversal of the binary tree
def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.val, end=" ")
        in_order_traversal(node.right)

#Usage with the given list
if __name__ == "__main__":
    linked_list = ListNode(1, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(8, ListNode(7, ListNode(9, ListNode(2, ListNode(22, ListNode(15, ListNode(55, 
    ListNode(45, ListNode(23, ListNode(24, ListNode(26, ListNode(28)))))))))))))))))
    root = sorted_list_to_bst(linked_list)
    in_order_traversal(root)

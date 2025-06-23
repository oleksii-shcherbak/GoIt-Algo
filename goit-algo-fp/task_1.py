class Node:
    """
    Represents a single node in a singly linked list.
    """
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    """
    Represents a singly linked list.
    """
    def __init__(self):
        self.head = None

    def append(self, value):
        """
        Appends a new node with the given value to the end of the list.
        """
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def print_list(self):
        """
        Prints all elements of the linked list.
        """
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements))

def reverse_linked_list(llist):
    """
    Reverses a singly linked list in-place by changing node pointers.

    Args:
        llist (LinkedList): The linked list to be reversed.
    """
    prev = None
    current = llist.head
    while current:
        next_node = current.next  # Store the next node
        current.next = prev       # Reverse the current node's pointer
        prev = current            # Move 'prev' to the current node
        current = next_node       # Move 'current' to the next node
    llist.head = prev  # Update the head of the list to the new first node

def get_middle(head):
    """
    Helper function to find the middle node of a linked list.
    Used by merge_sort_linked_list.

    Args:
        head (Node): The head of the linked list or sub-list.

    Returns:
        Node: The middle node of the list.
    """
    if not head:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def merge_sorted_lists(l1, l2):
    """
    Merges two already sorted singly linked lists into a single sorted list.

    Args:
        l1 (LinkedList): The first sorted linked list.
        l2 (LinkedList): The second sorted linked list.

    Returns:
        LinkedList: A new linked list containing all elements from l1 and l2,
                    sorted in ascending order.
    """
    # Create a dummy node to simplify the merging process
    dummy = Node()
    current = dummy

    head1 = l1.head
    head2 = l2.head

    while head1 and head2:
        if head1.value <= head2.value:
            current.next = head1
            head1 = head1.next
        else:
            current.next = head2
            head2 = head2.next
        current = current.next

    # Attach the remaining elements from either list (if any)
    if head1:
        current.next = head1
    elif head2:
        current.next = head2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

def merge_sort_linked_list(llist):
    """
    Sorts a singly linked list using the merge sort algorithm.

    Args:
        llist (LinkedList): The linked list to be sorted.

    Returns:
        LinkedList: A new linked list that is a sorted version of the input.
    """
    if not llist.head or not llist.head.next:
        return llist # Base case: list is empty or has one node

    # Split the list into two halves
    middle_node = get_middle(llist.head)
    next_to_middle = middle_node.next
    middle_node.next = None # Break the link to separate the two halves

    left_half = LinkedList()
    left_half.head = llist.head

    right_half = LinkedList()
    right_half.head = next_to_middle

    # Recursively sort both halves
    left_sorted = merge_sort_linked_list(left_half)
    right_sorted = merge_sort_linked_list(right_half)

    # Merge the sorted halves
    merged_list = merge_sorted_lists(left_sorted, right_sorted)
    return merged_list

# Example Usage
if __name__ == "__main__":
    print("Original List for Reversal:")
    llist1 = LinkedList()
    for i in range(1, 5):
        llist1.append(i)
    llist1.print_list()

    print("\nReversed List:")
    reverse_linked_list(llist1)
    llist1.print_list()

    print("\nOriginal List for Sorting:")
    llist_unsorted = LinkedList()
    unsorted_values = [38, 27, 43, 3, 9, 82, 10]
    for value in unsorted_values:
        llist_unsorted.append(value)
    llist_unsorted.print_list()

    print("\nSorted List (Merge Sort):")
    sorted_llist = merge_sort_linked_list(llist_unsorted)
    sorted_llist.print_list()

    print("\nFirst Sorted List for Merging:")
    llist_a = LinkedList()
    sorted_values_a = [1, 5, 7]
    for value in sorted_values_a:
        llist_a.append(value)
    llist_a.print_list()

    print("\nSecond Sorted List for Merging:")
    llist_b = LinkedList()
    sorted_values_b = [2, 3, 6, 8]
    for value in sorted_values_b:
        llist_b.append(value)
    llist_b.print_list()

    print("\nMerged Sorted Lists:")
    merged_llist = merge_sorted_lists(llist_a, llist_b)
    merged_llist.print_list()

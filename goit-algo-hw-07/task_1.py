class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def insert(root, key):
    """Insert a new key into the Binary Search Tree."""
    if root is None:
        return Node(key)
    else:
        if key < root.val:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root


def find_max_value(root):
    """
    Find the maximum value in a Binary Search Tree.

    Args:
        root: The root node of the BST

    Returns:
        The maximum value in the tree, or None if tree is empty
    """
    if root is None:
        return None

    current = root
    while current.right is not None:
        current = current.right

    return current.val


def print_inorder(root):
    """Print the BST in inorder traversal"""
    if root:
        print_inorder(root.left)
        print(root.val, end=" ")
        print_inorder(root.right)


# Test the implementation
if __name__ == "__main__":
    # Create a sample BST
    root = Node(50)
    root = insert(root, 30)
    root = insert(root, 20)
    root = insert(root, 40)
    root = insert(root, 70)
    root = insert(root, 60)
    root = insert(root, 80)
    root = insert(root, 90)
    root = insert(root, 10)

    print("Binary Search Tree (inorder traversal):")
    print_inorder(root)
    print()

    # Find maximum value
    max_value = find_max_value(root)
    print(f"Maximum value: {max_value}")

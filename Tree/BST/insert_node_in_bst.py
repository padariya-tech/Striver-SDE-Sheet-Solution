class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


class BST:
    def insert(self, root, key):
        # If the current position is empty, insert here
        if root is None:
            return Node(key)

        # If key is smaller, insert into the left subtree
        if key < root.data:
            root.left = self.insert(root.left, key)

        # If key is greater, insert into the right subtree
        elif key > root.data:
            root.right = self.insert(root.right, key)

        return root


def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


if __name__ == "__main__":
    bst = BST()
    root = None

    values = [50, 30, 70, 20, 40, 60, 80]

    for val in values:
        root = bst.insert(root, val)

    print("Inorder before insertion:")
    inorder(root)

    key = 65
    root = bst.insert(root, key)

    print("\nInorder after insertion:")
    inorder(root)
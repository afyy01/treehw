class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def preorder_traversal(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=' ')

def main_menu():
    while True:
        print("\n . Binary Tree Operations Menu .")
        print("1. Create a Binary Tree")
        print("2. Insert an Element")
        print("3. Preorder Traversal")
        print("4. Inorder Traversal")
        print("5. Postorder Traversal")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            bt = BinaryTree()
            print("Binary Tree created successfully!")

        elif choice == '2':
            element = int(input("Enter the element to insert: "))
            bt.insert(element)
            print(f"Inserted {element} into the tree.")

        elif choice == '3':
            if bt.root is not None:
                print("Preorder Traversal: ", end='')
                bt.preorder_traversal(bt.root)
                print()  # New line after traversal
            else:
                print("Tree is empty!")

        elif choice == '4':
            if bt.root is not None:
                print("Inorder Traversal: ", end='')
                bt.inorder_traversal(bt.root)
                print()  # New line after traversal
            else:
                print("Tree is empty!")

        elif choice == '5':
            if bt.root is not None:
                print("Postorder Traversal: ", end='')
                bt.postorder_traversal(bt.root)
                print()  # New line after traversal

if __name__ == "__main__":
    main_menu()

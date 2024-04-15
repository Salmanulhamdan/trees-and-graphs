# class TreeNode:
#     def __init__(self,key) -> None:
#         self.key=key
#         self.left=None
#         self.right=None

# class BinarysearchTree:
#     def __init__(self) -> None:
#         self.root=None

#     def insert(self,root,key):
#         if root is None:
#             return TreeNode(key)

#         else:
#             if root.key==key:
#                 return root
#             elif root.key< key:
#                 root.right = self.insert(root.right,key)
#             else:
#                 root.left =self.insert(root.left,key)
#         return root

    
#     def inorder(self,root):
#         if root is None:
#             return -1
#         else:
#             self.inorder(root.left)
#             print(root.key)
#             self.inorder(root.right)

# demo=BinarysearchTree()
# root=None
# root=demo.insert(root,50)
# root=demo.insert(root,11)
# root=demo.insert(root,23)
# root=demo.insert(root,57)
# root=demo.insert(root,20)
# root=demo.insert(root,40)
# root=demo.insert(root,5)

# demo.inorder(50)


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        else:
            if key < root.val:
                root.left = self.insert(root.left, key)
            else:
                root.right = self.insert(root.right, key)
        return root

    # def search(self, root, key):
    #     if root is None or root.val == key:
    #         return root
    #     if key < root.val:
    #         return self.search(root.left, key)
    #     return self.search(root.right, key)

    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(root.val)
            self.inorder_traversal(root.right)

# Example usage
# if __name__ == "__main__":
bst = BinarySearchTree()
root = None
root = bst.insert(root, 50)
root = bst.insert(root, 30)
root = bst.insert(root, 20)
root = bst.insert(root, 40)
root = bst.insert(root, 70)
root = bst.insert(root, 60)
root = bst.insert(root, 80)

print("Inorder traversal:")
bst.inorder_traversal(root)

    # Search for a key
    # key_to_search = 60
    # if bst.search(root, key_to_search):
    #     print(f"Key {key_to_search} found in the BST.")
    # else:
    #     print(f"Key {key_to_search} not found in the BST.")

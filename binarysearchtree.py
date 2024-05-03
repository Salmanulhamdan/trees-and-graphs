class TreeNode:
    def __init__(self,key) -> None:
        self.key=key
        self.right=None
        self.left=None
    

class BinarySearchTree:
    def __init__(self) -> None:
        self.root=None

    def insert(self,root,key):
        if root is None:
            return TreeNode(key)
        else:
            if key < root.key:
                root.left=self.insert(root.left,key)
            else:
                root.right=self.insert(root.right,key)

        return root
    
    def search(self,root,key):
        if root is None or root.key==key:
            return root,print(root.key)
        if root.key<key:
            return self.search(root.right,key)
        return self.search(root.left,key)

    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.key)
            self.inorder(root.right)

    def preorder(self,root):
        if root:
            print(root.key)
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.key)

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node with only one child or no child
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            # Node with two children: Get the inorder successor
            temp = self.min_value_node(root.right)

            # Copy the inorder successor's content to this node
            root.key = temp.key

            # Delete the inorder successor
            root.right = self.delete(root.right, temp.key)

        return root

    def min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current




demo=BinarySearchTree()


root=None
root=demo.insert(root,40)
root=demo.insert(root,4)
root=demo.insert(root,61)
root=demo.insert(root,52)
root=demo.insert(root,70)
root=demo.insert(root,8)
root=demo.insert(root,20)

demo.inorder(root)

print("-------------")

demo.preorder(root)
print("-------------")

demo.postorder(root)
print("-------------")
key_to_search = 70
demo.delete(root, 20)
demo.postorder(root)
print("-------------")


    
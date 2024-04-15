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




    
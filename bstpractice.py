class TreeNode:
    def __init__(self,key) -> None:
        self.key=key
        self.left=None
        self.right=None


class Tree:
    def __init__(self) -> None:
        self.root=None

    def add(self,root,key):
        
        if root is None:
            return TreeNode(key)
        else:
            if key< root.key:
                root.left=self.add(root.left,key)
            else:
                root.right=self.add(root.right,key)
        return root
    
    def inorder(self,root):
        traversal=[]
        if root:
            traversal+=self.inorder(root.left)
            traversal.append(root.key)
            traversal+=self.inorder(root.right)

        return traversal
    
    def preorder(self,root):
        traversal=[]
        if root:
            traversal.append(root.key)
            traversal+=self.preorder(root.left)
            traversal+=self.preorder(root.right)
        return traversal
     
    
demo=Tree()

demo.root = demo.add(demo.root, 4)
demo.add(demo.root,2)
demo.add(demo.root,3)
demo.add(demo.root,7)
demo.add(demo.root,8)
demo.add(demo.root,1)

print(demo.inorder(demo.root))
print(demo.preorder(demo.root))
    





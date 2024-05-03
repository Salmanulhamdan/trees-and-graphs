class Bts:
    def __init__(self,value) -> None:

        self.value=value
        self.right=None
        self.left=None


class BinaryST:
    def __init__(self) -> None:
        self.root=None

    def add(self,root,value):
        if root is None:
            return Bts(value)
        else:
            if root.value< value:
                root.right=self.add(root.right,value)
            else:
                root.left=self.add(root.left,value)
        return root
        

    def delete(value):
        pass

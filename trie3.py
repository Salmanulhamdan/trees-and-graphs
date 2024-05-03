class Trinode:
    def __init__(self) -> None:
        self.children={}
        self.is_end_of_word=False


class Trie:
    def __init__(self) -> None:
        self.root=Trinode()

    def insert(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=Trinode()
            node=node.children[ch]
        node.is_end_of_word=True


    def search(self,word):
        node=self.root
        for ch in word:
            if ch not in node.children:
                return False
            node=node.children[ch]
        return node.is_end_of_word
    
    def delete(self,word):
        node=self.root
        
    

    
    
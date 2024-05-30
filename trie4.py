class Trinode:
    def __init__(self) -> None:
        self.children={}
        self.end_word=False


class Trie:
    def __init__(self) -> None:
        self.root=Trinode()

    def insert(self,word):
        node =self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch]=Trinode()
            node=node.children[ch]
        node.end_word=True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.end_word
    


    def prefix_search(self, prefix: str) -> list[str]:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []

            node = node.children[ch]

        words = []
        stack = [(node, prefix)]

        while stack:
            current_node, current_prefix = stack.pop()

            if current_node.end_word:
                words.append(current_prefix)

            for ch, child in current_node.children.items():
                stack.append((child, current_prefix + ch))

        return words


     # removes a word from the trie and trims unnecessary branches
    def delete(self, word: str) -> None:
        root = self.root
        path = []

        # Search through the trie, tracking your path
        for c in word:
            path.append((root, c))
            try:
                root = root.children[c]
            except KeyError:
                print('Word is not in trie')
                return

        # Get rid of the end marker, if it's present
        if root.end_word:
            root.end_word = False
        else:
            print('Word is not in trie')
            return

        # If there are no more children, backtrack through the trie, trimming your branch
        while path:
            node, c = path.pop()
            if not node.children[c].children and not node.children[c].end_word:
                del node.children[c]
            else:
                break



    

    


demo=Trie()

demo.insert("hamdan")
demo.insert("hamd")
demo.insert("haskeda")
demo.insert("pokeda")
demo.insert("leeda")
demo.insert("alpp")

print(demo.search("hamdan"))

# demo.delete("hamdan")


print(demo.search("hamdan"))
print(demo.prefix_search("h"))




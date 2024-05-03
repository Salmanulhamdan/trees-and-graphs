class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def prefix_search(self, prefix: str) -> list[str]:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return []
            node = node.children[ch]

        words = []
        self._dfs(node, prefix, words)
        return words

    def _dfs(self, node: TrieNode, prefix: str, words: list[str]) -> None:
        if node.is_end:
            words.append(prefix)

        for ch, child in node.children.items():
            self._dfs(child, prefix + ch, words)
trie = Trie()
trie.insert("hello")
trie.insert("world")
trie.insert("hi")
trie.insert("hey")
print(trie.prefix_search("h"))
print(trie.prefix_search("he"))
print(trie.prefix_search("w"))
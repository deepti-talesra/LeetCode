class Trie:
    def __init__(self):
        self.children = {}
        self.word = False

    def insert(self, word: str) -> None:
        root = self
        for char in word:
            if char not in root.children:
                root.children[char] = Trie()
            root = root.children[char]
        root.word = True

    def search(self, word: str) -> bool:
        root = self
        for char in word:
            if char not in root.children:
                return False
            root = root.children[char]
        return root.word

    def startsWith(self, prefix: str) -> bool:
        root = self
        for char in prefix:
            if char not in root.children:
                return False
            root = root.children[char]
        return True

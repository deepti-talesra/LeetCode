class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
        curr.word = True

    def search(self, word: str) -> bool:
        def dfs(i, root):
            if i == len(word):
                return root.word
            if word[i] == ".":
                for letter in root.children.values():
                    if dfs(i+1, letter):
                        return True
                return False
            else:
                if word[i] not in root.children:
                    return False
                return dfs(i+1, root.children[word[i]])
        return dfs(0, self.root)
# # Your WordDictionary object will be instantiated and called as such:
# # obj = WordDictionary()
# # obj.addWord(word)
# # param_2 = obj.search(word)

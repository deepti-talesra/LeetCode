class TrieNode:
    def __init__(self):
        self.children = {}
        self.product = []

        
class Solution:
    def __init__(self):
        self.root = TrieNode()
        
        
    def add(self, word):
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            if len(curr.product) < 3:
                curr.product.append(word)
        return 
    
    
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        output = [[] for char in searchWord]
        products.sort()
        for word in products:
            self.add(word)
        curr = self.root
        for i, char in enumerate(searchWord):
            if char not in curr.children:
                break
            curr = curr.children[char]
            output[i] = curr.product
                
        return output

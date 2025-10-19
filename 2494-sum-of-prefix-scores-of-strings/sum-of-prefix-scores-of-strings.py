class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False
        self.count = 0
    
    def insert(self, word):
        cur = self
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
            cur.count += 1
        cur.endOfWord = True
    
    def getPrefixScore(self, word):
        cur = self
        score = 0
        for c in word:
            cur = cur.children[c]
            score += cur.count
        return score

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()

        for word in words:
            root.insert(word)
        
        res = []
        for word in words:
            res.append(root.getPrefixScore(word))
        
        return res
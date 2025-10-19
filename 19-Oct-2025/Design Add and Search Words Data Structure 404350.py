# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c] 
        cur.is_word = True
    def search(self, word: str) -> bool:
        def dfs(idx, cur):
            if idx == len(word):
                return cur.is_word
            c = word[idx]
            if c == '.':
                for i in cur.children.values():
                    if dfs(idx+1, i):
                        return True
                return False
                    
            else:
                if c not in cur.children:
                    return False
                return dfs(idx+1, cur.children[c])
        # cur = self.root
        return dfs(0, self.root)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
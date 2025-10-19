# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        ans = []
        class Tries:
            def __init__(self):
                self.root = TrieNode()
            def insert(self, word):
                cur = self.root
                for c in word:
                    if not c in cur.children:
                        cur.children[c] = TrieNode()
                    cur = cur.children[c]
                cur.is_word = True
            def findroot(self, word):
                cur = self.root
                prefix = ""
                for c in word:
                    if c not in cur.children:
                        return word
                    cur = cur.children[c]
                    prefix += c
                    if cur.is_word:
                        return prefix
                return word
                        
        
        tries = Tries()
        for root in dictionary:
            tries.insert(root)
        sent_arr = sentence.split(' ')
        for word in sent_arr:
            ans.append(tries.findroot(word))
        return " ".join(ans)
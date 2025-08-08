# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class DSU:
    def __init__(self):
        self.equ = {chr(ord('a')+i):chr(ord('a')+i) for i in range(26)}
    def find(self, char):
        if self.equ[char] != char:
            self.equ[char] = self.find(self.equ[char])
        return self.equ[char]
    def union(self, x, y):
        s_equx = self.find(x)
        s_equy = self.find(y)
        if s_equx != s_equy:
            rep = min(s_equx, s_equy)
            self.equ[s_equx] = rep
            self.equ[s_equy] = rep
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dsu = DSU()
        ans = []
        for i in range(len(s1)):
            dsu.union(s1[i],s2[i])
        for char in baseStr:
            ans.append(dsu.find(char))
        return "".join(ans)
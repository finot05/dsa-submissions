# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for char in s:
            if char != ']':
                stk.append(char)
            else:
                string = ""
                while stk and stk[-1] != '[':
                    string = stk.pop() + string 
                stk.pop()
                k = ""
                while stk and stk[-1].isdigit():
                    k = stk.pop() + k
                stk.append(int(k)*string)
        return ''.join(stk)
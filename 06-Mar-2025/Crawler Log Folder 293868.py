# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stk = []
        for path in logs:
            if path == '../':
                if stk:
                    stk.pop()
            elif path != './':
                stk.append(path)
        return len(stk)
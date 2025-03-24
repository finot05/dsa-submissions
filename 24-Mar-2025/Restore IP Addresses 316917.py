# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.ans = []
        def partition(i, path):
            if i == len(s):
                if len(path) == 4:
                    self.ans.append('.'.join(path))
                return 
            for j in range(i, len(s)):
                string = s[i:j+1]
                if len(string) > 1 and string[0] == '0':
                    break
                if int(string) <= 255:
                    path.append(string)
                    partition(j+1, path)
                    path.pop()
                else:
                    break
        partition(0, [])
        return self.ans
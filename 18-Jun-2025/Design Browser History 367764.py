# Problem: Design Browser History - https://leetcode.com/problems/design-browser-history/description/

class linkedlist:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = linkedlist(homepage)

    def visit(self, url: str) -> None:
        
        node = linkedlist(url)
        self.cur.next = node
        node.prev = self.cur
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while steps > 0 and self.cur.prev:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps: int) -> str:
        while steps > 0 and self.cur.next:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
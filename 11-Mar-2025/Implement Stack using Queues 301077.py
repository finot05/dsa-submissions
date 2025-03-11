# Problem: Implement Stack using Queues - https://leetcode.com/problems/implement-stack-using-queues/

class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()
    def push(self, x: int) -> None:
        self.q1.append(x)

    def pop(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_element = self.q1.popleft() 
        self.q1, self.q2 = self.q2, self.q1  
        return top_element

    def top(self) -> int:
        while len(self.q1) > 1:
            self.q2.append(self.q1.popleft())
        top_element = self.q1[0]
        self.q2.append(self.q1.popleft()) 
        self.q1, self.q2 = self.q2, self.q1 
        return top_element

    def empty(self) -> bool:
        return not self.q1


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
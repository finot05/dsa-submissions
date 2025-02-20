# Problem: Design Linked List - https://leetcode.com/problems/design-linked-list/

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index: int) -> int:
        counter = 0
        current = self.head
        while current:
            if counter == index:
                return current.val
            counter += 1
            current = current.next
        return -1

    def addAtHead(self, val: int) -> None:
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode

    def addAtTail(self, val: int) -> None:
        newNode = Node(val)
        if not self.head:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def addAtIndex(self, index: int, val: int) -> None:
        newNode = Node(val)
        if index == 0:
            self.addAtHead(val)
            return
        current = self.head
        for _ in range(index - 1):
            if current is None:
                return  
            current = current.next
        if current:
            newNode.next = current.next
            current.next = newNode

    def deleteAtIndex(self, index: int) -> None:
        if not self.head:
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        for _ in range(index - 1):
            if current is None or current.next is None:
                return  
            current = current.next
        if current.next:
            current.next = current.next.next

    def printLinkedList(self):
        llist = []
        current = self.head
        while current:
            llist.append(current.val)
            current = current.next
        print(llist)

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
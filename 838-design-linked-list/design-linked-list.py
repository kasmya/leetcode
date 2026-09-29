class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None

    def get(self, index):
        cur = self.head
        while cur and index > 0:
            cur = cur.next
            index -= 1
        return cur.val if cur else -1


    def addAtHead(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node


    def addAtTail(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = node


    def addAtIndex(self, index, val):
        if index == 0:
            self.addAtHead(val)
            return
        cur = self.head
        while cur and index > 1:
            cur = cur.next
            index -= 1
        if cur is None:
            return
        node = Node(val)
        node.next = cur.next
        cur.next = node


    def deleteAtIndex(self, index):
        if self.head is None:
            return
        if index == 0:
            self.head = self.head.next
            return
        cur = self.head
        while cur.next and index > 1:
            cur = cur.next
            index -= 1
        if cur.next:
            cur.next = cur.next.next
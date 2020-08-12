class ListNode:
    def __init__(self, value):
        self.next = None
        self.data = value
class CircularLinkedList:
    def __init__(self):
        self.last = None

    def insertAtEnd(self, newNode):
        if self.last is None:
            self.last = newNode
            self.last.next = self.last
        else:
            newNode.next = self.last.next
            self.last.next = newNode
            self.last = newNode
        return self.last

    def push(self,newNode):
        if self.last is None:
            self.last = newNode
            self.last.next = self.last
        else:
            newNode.next = self.last.next
            self.last.next = newNode
        return self.last

    def printList(self):
        temp = self.last.next
        while temp != self.last:
            print(temp.data, end = ' ')
            temp = temp.next
        print(temp.data)


csll = CircularLinkedList()
csll.insertAtEnd(ListNode(1))
csll.insertAtEnd(ListNode(2))
csll.insertAtEnd(ListNode(3))
csll.insertAtEnd(ListNode(4))
csll.insertAtEnd(ListNode(5))
csll.printList()
csll.push(ListNode(20))
csll.printList()

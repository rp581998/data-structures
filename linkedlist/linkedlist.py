class ListNode:
    def __init__(self, value):
        self.next = None
        self.data = value
class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtEnd(self, node):
        if self.head is None:
            self.head = node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node
        return self.head
    
    def printList(self):
        if self.head:
            temp = self.head
            while temp is not None:
                print(temp.data, end = ' ')
                temp = temp.next
        print()
    def push(self, node):
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node
        return self.head
    def insertAt(self, position, node):
        if self.head:
            count = 0
            temp = self.head
            while count < position - 1:
                temp = temp.next
                count +=1
            node.next = temp.next
            temp.next = node
        return self.head

    def middleOfList(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data


node = ListNode(1)
list = LinkedList()
list.insertAtEnd(node)
list.insertAtEnd(ListNode(2))
list.insertAtEnd(ListNode(3))
list.insertAtEnd(ListNode(4))
list.insertAtEnd(ListNode(5))
list.printList()
list.push(ListNode(10))
list.printList()
list.insertAt(4,ListNode(11))
list.printList()
print(list.middleOfList())

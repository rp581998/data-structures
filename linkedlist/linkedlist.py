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

    def deleteNode(self, key):
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return self.head
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return self.head
        prev.next = temp.next
        temp = None

    def middleOfList(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        i = 0
        temp = self.head
        while i < count//2:
            temp = temp.next
            i+=1
        return temp

        """              
              OR
        def middleOfList(self):
            a = []
        while head:
            a.append(head)
            head = head.next
        return a[len(a)//2]

                OR
        def middleOfList(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
        
        """


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
middleNode = list.middleOfList()
print(middleNode.data)

class ListNode:
    def __init__(self,value):
        self.next = None
        self.prev = None
        self.data = value
class doublyLinkedlist:
    def __init__(self):
        self.head = None

    def push(self, newNode):
        if self.head is None:
            self.head = newNode
            return self.head
        else:
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
            return self.head
    """
    // OR use this when you pass only the value
    def push(self, newValue):
        newNode = ListNode(newValue)
        if self.head is None:
            self.head = newNode
            return self.head
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            return self.head
    """
    def getLength(self):
        temp = self.head
        count = 1
        while temp is not None:
            temp = temp.next
            count += 1
        return count
    def insertAtLast(self,newNode):
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = newNode
            newNode.prev = temp
            return self.head

    def insertAtPosition(self,position,newNode):
        len = self.getLength()
        if position > len or position < 0:
            print("Position is greater than length of doubly linked list or less")
        else:
            if position == 0:
                self.head = self.push(newNode)
            else:
                if position == len:
                    self.head = self.insertAtLast(newNode)
                else:
                    count = 0
                    temp = self.head
                    while count < position -1:
                        prev = temp
                        temp = temp.next
                        count += 1
                    newNode.next = temp
                    prev.next = newNode
                return self.head
    
    def deleteBiginning(self):
        len = self.getLength()
        if len == 0:
            print("list is empty")
        else:
            temp = self.head
            self.head = self.head.next
            self.head.prev = None
            temp = None

    def deleteLastNode(self):
        len = self.getLength()
        if len == 0:
            print('list is empty')
        else:
            current = self.head
            previous = self.head
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
            current = None
        

    def reverseDLL(self):
        temp = None
        current = self.head
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev
            return self.head
    
    def middleOfList(self):
        arr = []
        while self.head.next is not None:
            arr.append(self.head.data)
            self.head = self.head.next
        return arr[len(arr)//2]


    def printlist(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()


dllist = doublyLinkedlist()
'''
dllist.push(1)
dllist.push(0)
'''
dllist.push(ListNode(1))
dllist.push(ListNode(2))
dllist.push(ListNode(3))
dllist.printlist()
#dllist.deleteBiginning()
#dllist.printlist()
dllist.deleteLastNode()
dllist.printlist()
#dllist.reverseDLL()
#dllist.printlist()
#dllist.insertAtLast(ListNode(4))
#dllist.insertAtLast(ListNode(10))
#dllist.printlist()
#print(dllist.middleOfList())
#dllist.insertAtPosition(-1, ListNode(11))

#dllist.printlist()
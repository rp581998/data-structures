class ListNode:
    def __init__(self, value):
        self.next = None
        self.data = value
class LinkedList:
    def __init__(self):
        self.head = None
    def insertAtEnd(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = newNode
        return self.head
    
    def printList(self):
        if self.head:
            temp = self.head
            while temp is not None:
                print(temp.data, end = ' ')
                temp = temp.next
        print()
    def push(self, newNode):
        if self.head is None:
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return self.head
    def getLength(self):
        temp = self.head
        count = 1
        while temp is not None:
            temp = temp.next
            count+=1
        return count
    def insertAt(self, position,newNode):
        len = self.getLength()
        if position > len or position < 0:
            print("Position is greater than length of linked list or less")
        else:
            if position == 0:
                self.head = self.push(newNode)
            else:
                if position == len:
                    self.head = self.insertAtEnd(newNode)
                else:
                    count = 0
                    temp = self.head
                    while count < position - 1:
                        prev = temp
                        temp = temp.next
                        count += 1
                    newNode.next = temp
                    prev.next = newNode
                return self.head


    def reverseLinkedList(self):
        prev = None
        current = self.head
        while current is not None:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        self.head = prev
        return self.head

    def delete_biginning(self):
        len = self.getLength()
        if len == 0:
            print ("List is empty")
        else:
            self.head = self.head.next
            len -= 1

    def deleteLastNode(self):
        len = self.getLength()
        if len == 0:
            print("List is empty")
        else:
            current = self.head
            previous = self.head
            while current.next is not None:
                previous = current
                current = current.next
            previous.next = None
            len -= 1 


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
        while self.head:
            a.append(self.head.data)
            self.head = self.head.next
        return a[len(a)//2]

                OR
        def middleOfList(self):
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
        
        """


#node = ListNode(1)
list = LinkedList()
list.insertAtEnd(ListNode(1))
list.insertAtEnd(ListNode(2))
list.insertAtEnd(ListNode(3))
list.insertAtEnd(ListNode(4))
list.insertAtEnd(ListNode(5))
list.insertAtEnd(ListNode(5))
list.printList()
list.push(ListNode(10))
list.printList()
list.delete_biginning()
list.printList()
list.deleteLastNode()
list.printList()
#list.insertAt(4,ListNode(11))

#list.insertAt(-1,ListNode(15))
#list.printList()
#middleNode = list.middleOfList()
#print(middleNode.data)
#list.reverseLinkedList()
#list.printList()

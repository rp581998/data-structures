'''
stack: A stack is an ordered list in which insertion and deletion are done at one end, called top. The last
element inserted is first one to be deleted. Hence, it is called the Last in first out (LIFO) or First
in last out (FILO) list. 
we implement tha stack thee type:
1: Simply Array implementation
2: Dynaminc Array based implementaion
3: Linked List Implemenation
'''
#                                       1: Simply Array implementation
'''
class Stack(object):
    def __init__(self,limit = 10):
        self.stack = []
        self.limit = limit

    def is_empty(self):
        return len(self.stack) <= 0

    def push(self, item):
        if len(self.stack) >= self.limit:
            print('Stack Overflow')
        else:
            self.stack.append(item)
        print('Stack after push', self.stack)

    def pop(self):
        if len(self.stack) <= 0:
            print('Stack underflow')
            return 0
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) <= 0:
            print('Stack underflow')
            return 0
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

'''
#                                      2: Dynaminc Array based implementaion
'''
class Stack(object):
    def __init__(self,limit = 10):
        self.stack = limit*[None]
        self.limit = limit

    def is_empty(self):
        return len(self.stack) <= 0

    def push(self, item):
        if len(self.stack) >= self.limit:
            self.resize()
        self.stack.append(item)
        print('Stack after push', self.stack)

    def pop(self):
        if len(self.stack) <= 0:
            print('Stack underflow')
            return 0
        else:
            return self.stack.pop()

    def peek(self):
        if len(self.stack) <= 0:
            print('Stack underflow')
            return 0
        else:
            return self.stack[-1]

    def size(self):
        return len(self.stack)

    def resize(self):
        newStack = list(self.stack)
        self.limit = 2*self.limit
        self.stack = newStack

'''


#                               3: Linked List Implemenation
'''
class ListNode:
    def __init__(self, data):
        self.next = None
        self.data = data

class Stack:
    def __init__(self):
        self.head = None

    def push(self, newNode):
        if self.head == None:
            self.head  =newNode
        else:
            newNode.next = self.head
            self.head = newNode
        return self.head

    def pop(self):
        if self.head is None:
            print('Stack Underflow')
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            return temp.data

    
    def printStack(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()

        


our_stack = Stack()
our_stack.push(ListNode(1))
our_stack.push(ListNode(2))
our_stack.push(ListNode(3))
our_stack.printStack()
#our_stack.pop()
#our_stack.printStack()
'''

def is_palindrome(string):
    newStack = []
    temp = ''
    for char in string:
        newStack.append(char)
    while len(newStack) != 0:
        temp += newStack.pop()
    if temp == string:
        return True
    else:
        return False

print(is_palindrome("rajar"))
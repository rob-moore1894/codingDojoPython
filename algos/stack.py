class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value):
        #create a new node
        newNode = Node(value)
        #if queue is empty, set self.head and self.tail to value
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = self.tail.next
        return self

    #dequeue means to remove from the head of the queue
    def dequeue(self):
        if self.head == None:
            print("Nothing to remove")
        else:
            self.head = self.head.next
            if self.head == None:
                self.tail = None
        return self

    def size(self):
        runner = self.head
        count = 0
        while runner != None:
            count += 1
            runner = runner.next
        print(count)
        return self

    def display(self):
        runner = self.head
        while runner != None:
            print(runner.value)
            runner = runner.next
        print(runner)
        return self

    def contains(self, val): 
        runner = self.head
        while runner != None:
            if runner.value == val:
                return True
            runner = runner.next
        return False

class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        newNode = Node(value)
        if self.top == None:
            self.top = newNode
        else: 
            newNode.next = self.top
            self.top = newNode
        return self

    def pop(self):
        if self.top == None:
            print('Stack is empty')
            return self
        else:
            returnVal = self.top.value
            self.top = self.top.next
        return returnVal

    def size(self):
        runner = self.top
        count = 0
        while runner != None:
            count += 1
            runner = runner.next
        print(count)
        return count

    def display(self):
        runner = self.top
        while runner != None:
            print(runner.value)
            runner = runner.next
        print(runner)
        return self

stk1 = Stack()
stk1.push(6).push(1).push(9).display()
stk1.display()

q1 = Queue()

q1.enqueue('h').enqueue('a').enqueue('n').enqueue('n').enqueue('a').enqueue('h')


def palindrome(queueInput):
    stk = Stack()
    length = queueInput.size()
    for i in range(length):
        t = queueInput.dequeue()
        queueInput.enqueue(t)
        stk.push(t)
    rnr = queueInput.head
    rnr2 = stk.top
    while rnr is not None:
        if rnr.value is not rnr2.value:
            print(False)
            return False
        rnr = rnr.next
        rnr2 = rnr2.next
    print(True)


palindrome(q1)

def copyStack(ogStack):
    q = Queue()
    result = Stack()
    length = ogStack.size()
    ogrunner = ogStack.top
    for i in range(0,length, 1):
        newnode = Node(ogrunner.value)
        result.push(newnode)
        ogrunner=ogrunner.next
    # print(result.top.value.value)
    for i in range(0, length, 1):
        newnode= Node(result.pop())
        q.enqueue(newnode)

    for i in range(0, length, 1):
        newnode = Node(q.dequeue())
        result.push(newnode)

    return result


stk1.push(23).push(6).push(8)

print(copyStack(stk1))
y = copyStack(stk1)
y.display()
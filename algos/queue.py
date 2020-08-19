class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    #enqueue means to add to the back of the queue
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
    
    def contain(self, val):
        runner = self.head
        while runner != None:
            if runner.value == val:
                return True
        return False


q1 = Queue()
q1.enqueue(5).enqueue(15).enqueue(25).display()
print("*****************************")
print(q1.contains(2))


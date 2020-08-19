class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

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

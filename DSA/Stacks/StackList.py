class Stack:
    def __init__(self):
        self.items = []
        self.length = 0

    def __str__(self):
        # values = [str(x) for x in self.items]
        return "(top) " + " ".join(map(str, reversed(self.items)))

    def is_empty(self):     ## O(1) time complexity
        return self.length == 0

    def push(self, value):  ## O(1) time complexity
        self.length += 1
        return self.items.append(value)

    def pop(self):  ## O(1) time complexity
        if self.length == 0:
            return "stack is empty"
        self.length -= 1
        return self.items.pop()

    def peek(self): ## O(1) time complexity
        if self.length == 0:
            return "stack is empty"
        return self.items[-1]

    def clear_all(self):    ## O(1) time complexity
        self.items = []
        self.length = 0




my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print(my_stack)
print(my_stack.peek())
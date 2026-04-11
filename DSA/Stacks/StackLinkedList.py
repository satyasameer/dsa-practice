class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0

    def __str__(self):
        if self.is_empty():
            return "Stack is Empty"
        values = ["(top)"]
        current = self.top
        while current:
            values.append(str(current.value))
            current = current.next
        return " ".join(values)

    def is_empty(self):
        return self.length == 0

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    def peek(self):
        return self.top

    def pop(self):
        if self.top is None:
            return "Stack is Empty"
        popped_node = self.top
        self.top = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def clear_all(self):
        self.top = None
        self.length = 0


my_stack = Stack()
my_stack.push(10)
my_stack.push(20)
my_stack.push(30)
print(my_stack)

print(my_stack.pop())
print(my_stack.peek())
print(my_stack)
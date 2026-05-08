class MinStack:

    def __init__(self):
        self.items = []
        self.minStack = []
        
    def push(self, val: int) -> None:
        self.items.append(val)
        if self.minStack and self.minStack[-1] < val:
            self.minStack.append(self.minStack[-1])
        else:
            self.minStack.append(val)
        

    def pop(self) -> None:
        if self.items == []:
            return
        self.items.pop()
        self.minStack.pop()
        

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
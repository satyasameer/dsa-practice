## Circular Queue implementation using List

class Queue:
    def __init__(self, maxSize):        ## O(1) time complexity
        self.items = [None] * maxSize
        self.start = -1
        self.top = -1
        self.maxSize = maxSize

    def __str__(self):
        return " ".join(map(str, self.items))

    def _queueInfo(self):
        print("queue elements: -> ", self)
        print("start: ", self.start)
        print("top: ", self.top)


    def isEmpty(self):      ## O(1) time complexity
        if self.top == -1:
            return True
        return False
    
    def isFull(self):       ## O(1) time complexity
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    def enqueue(self, value):       ## O(1) time complexity
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
                self.items[self.top] = value
        return f"{value} inserted at the end of the queue"

    def dequeue(self):      ## O(1) time complexity
        if self.isEmpty():
            return "queue is empty"
        else:
            start = self.start
            firstElement = self.items[self.start]
            self.items[start] = None
            if self.start == self.top:
                self.start = -1
                self.top = -1
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
        return firstElement
        
    def peek(self):         ## O(1) time complexity
        if self.isEmpty():
            return "queue is empty"
        else:
            return self.items[self.start]

customQueue = Queue(4)
print(customQueue.enqueue(1))
print(customQueue.enqueue(2))
print(customQueue.enqueue(3))
print(customQueue.enqueue(4))
print(customQueue.enqueue(5))
customQueue._queueInfo()
print(customQueue.dequeue())
print(customQueue.dequeue())
# print(customQueue.dequeue())
# print(customQueue.dequeue())
# print(customQueue.dequeue())
customQueue._queueInfo()
print(customQueue.peek())



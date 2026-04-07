class Node:
    def __init__(self, value):
        self.val = value
        self.next: Node | None = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        

    def get(self, index: int) -> int:
        if index < 0 or index >= self.length:
            return -1
        count = 0
        current = self.head
        while current is not None:
            if count == index:
                return current.val
            current = current.next
            count += 1
        return -1
    

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1


    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        new_node = Node(val)
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            return self.addAtHead(val)
        elif index == self.length:
            return self.addAtTail(val)
        else:
            prev_node = self.head
            for _ in range(index-1):
                prev_node = prev_node.next
            new_node.next = prev_node.next 
            prev_node.next = new_node
            self.length += 1
        
    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.length:
            return None
        elif self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            del_node = self.head
            self.head = del_node.next
            del_node.next = None
        elif index == self.length - 1:
            prev_node = self.head
            while prev_node.next is not self.tail:
                prev_node = prev_node.next
            del_node = prev_node.next
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node = self.head
            for _ in range(index-1):
                prev_node = prev_node.next
            del_node = prev_node.next
            prev_node.next = del_node.next
            del_node.next = None
        self.length -= 1


        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.value))
            current = current.next
        return " <=> ".join(result)

    def _validate(self):
        count = 0
        if self.head is None or self.tail is None:
            assert self.head is None
            assert self.tail is None
        else:
            assert self.head.prev is None
            assert self.tail.next is None
            prev = None
            current = self.head

            while current is not None:
                # Check backward consistency
                assert current.prev == prev

                # Check forward consistency
                if current.next is not None:
                    assert current.next.prev == current
                else:
                    assert current == self.tail

                prev = current
                current = current.next
                count += 1

        assert count == self.length

        return True


    def append(self, value):    ## O(1) time complexity
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        self._validate()

    def prepend(self, value):   ## O(1) time complexity
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        self._validate()

    def insert(self, index, value):   ## O(n) time complexity
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            self.prepend(value)
            return True
        elif index == self.length:
            self.append(value)
            return True
        else:
            new_node = Node(value)
            prev = self.head
            for _ in range(index-1):
                prev = prev.next
            new_node.next = prev.next
            new_node.prev = prev
            prev.next.prev = new_node
            prev.next = new_node
        self.length += 1
        self._validate()



    def search(self, value): ## O(n) time complexity
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def get(self, index): ## O(n) time complexity
        if index < 0 or index >= self.length:
            return -1
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length-1,index,-1):
                current = current.prev
        return current

    def set(self, index, value): ## O(n) time complexity
        if index < 0 or index >= self.length:
            return False
        else:
            current = self.get(index)
            if current:
                current.value = value
                self._validate()
                return True
        return False

    def popfirst(self):     ## O(1) time complexity
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            del_node = self.head
            del_node.next.prev = None
            self.head = del_node.next
            del_node.next = None
        self.length -= 1
        self._validate()
    
    def pop(self):  ## O(1) time complexity
        if self.tail is None:
            return
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            del_node = self.tail
            del_node.prev.next = None
            self.tail = del_node.prev
            del_node.prev = None
        self.length -= 1
        self._validate()



    def remove(self, index): ## O(n) time complexity
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            self.popfirst()
            return True
        if index == self.length -1:
            self.pop()
            return True
        prev = self.head
        for _ in range(index-1):
            prev = prev.next
        del_node = prev.next
        prev.next = del_node.next
        del_node.next.prev = prev
        del_node.next = None
        del_node.prev = None
        self.length -= 1
        self._validate()







dll = DoubleLinkedList()
for i in range(5):
    dll.append(i*10)

# dll.prepend(-10)
print(dll)
# print(dll.get(0).value)
# print(dll.insert(6,15))
# dll.popfirst()
# dll.pop()
dll.remove(4)
print(dll)
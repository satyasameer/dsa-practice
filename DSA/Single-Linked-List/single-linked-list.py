
class Node:
    def __init__(self, value):
        self.value = value
        self.next: Node | None = None

class SingleLinkedListEmpty:
    def __init__(self):
        self.head: Node | None = None
        self.tail: Node | None = None
        self.length = 0
    
    def __str__(self):
        current = self.head
        result = ''
        while current is not None:
            result += str(current.value)
            if current.next is not None:
                result += "->"
            current = current.next
        return result
    
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

class SingleLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        current = self.head
        result = []
        while current is not None:
            result.append(str(current.value))
            # if current.next is not None:
            #     result += "->"
            current = current.next
        return "->".join(result)
    
    def _validate(self):
        if self.length == 0:
            assert self.head is None and self.tail is None
        else:
            assert self.head is not None
            assert self.tail is not None
            assert self.tail.next is None
    
    def append(self, value):        ## O(1) time complexity / O(1) space complexity
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):       ## O(1) time complexity / O(1) space complexity
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert(self, index, value):         ## O(n) time complexity / O(1) space complexity
        new_node = Node(value)
        if index < 0 or index > self.length:
            return False
        elif self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self.length += 1
        return True

    def traversal(self):        ## O(n) time complexity / O(1) space complexity
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    def search(self, value):    ## O(n) time complexity / O(1) space complexity
        current = self.head
        index = 0
        while current is not None:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return -1

    def get(self, index):        ## O(n) time complexity / O(1) space complexity
        current = self.head
        if index < -1 or index >= self.length:
            return None
        elif index == -1:
            return self.tail
        else:
            for _ in range(index):
                current = current.next
        return current
    
    def set(self, index, value):    ## O(n) time complexity / O(1) space complexity
        current = self.get(index)
        if current is not None:
            current.value = value
            return True
        return False

    def popfirst(self):     ## O(1) time complexity / O(1) space complexity
        if self.length == 0:
            return None
        pop_node = self.head
        if self.length == 1:
            self.tail = None
            self.head = None
        else:
            self.head = self.head.next
            pop_node.next = None
        self.length -= 1
        return pop_node

    def pop(self):          ## O(n) time complexity / O(1) space complexity
        if self.length == 0:
            return None
        pop_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            current = self.head
            while current.next is not self.tail:
                current = current.next
            self.tail = current
            current.next = None
        self.length -= 1
        return pop_node
    
    def remove(self, index):    ## O(n) time complexity / O(1) space complexity
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.popfirst().value ## O(1)
        elif index == self.length - 1:
            return self.pop().value       ## O(n)
        else:
            # current = self.head
            # for _ in range(index-1):
            #     current = current.next
            prev_node = self.get(index-1)   ## O(n)
            del_node = prev_node.next
            prev_node.next = del_node.next
        del_node.next = None
        self.length -= 1
        return del_node.value
        
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def reverse(self):
        if self.length <= 1:
            return False
        
        prev = None         ## 1-2-3-4-None  4-3-2-1-None
        current = self.head
        self.tail = self.head

        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        self._validate()
        return True
            

# new_node = Node(10)
# print(new_node)

new_linked_list = SingleLinkedList(0)
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.prepend(40)
# new_linked_list.insert(5,50)
# new_linked_list.insert(2,60)
print(new_linked_list)
#print(new_linked_list.search(50))
#new_linked_list.traversal()
#print(new_linked_list.get(2))
#new_linked_list.set(-1,90)
#print(new_linked_list)
# print(new_linked_list.pop())
# print(new_linked_list.remove(6))
# print(new_linked_list.tail.value)
print(new_linked_list.reverse())
# print(new_linked_list.head.value)
# print(new_linked_list.tail.value)
print(new_linked_list)



# new_empty_linked_list = SingleLinkedListEmpty()
# new_empty_linked_list.prepend(10)
# new_empty_linked_list.prepend(20)
# print(new_empty_linked_list)

class Node:
    def __init__(self, value):
        self.value = value
        self.next: None | Node = None

class CSLinkedList:
    def __init__(self) -> None:
        self.head: None | Node = None
        self.tail: None | Node = None
        self.length: int = 0
    
    def __str__(self):
        current = self.head
        result = []
        while current is not None:
            result.append(str(current.value))
            current = current.next
            if current == self.head:
                break
        return "->".join(result)

    def print_linked_list(self):
        if self.head and self.tail:
            print("CSLL: ",self.__str__())
            print("head: ", self.head.value)
            print("tail: ", self.tail.value)
            print("tail next: ", self.tail.next.value)
        else:
            print("Circular Single Linked List is empty!!")
    
    def append(self, value):  ## O(1) time complexity
        new_node = Node(value)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1
    
    def prepend(self, value):  ## O(1) time complexity
        new_node = Node(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1

    def insert(self, index, value):   ## O(n) time complexity
        if index < 0 or index > self.length:
            return 
        new_node = Node(value)
        if index == 0:
            if self.head is None:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.tail.next = new_node
                self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            prev_node = self.head
            for _ in range(index-1):
                prev_node = prev_node.next
            # print(prev_node.value)
            new_node.next = prev_node.next
            prev_node.next = new_node
        self.length += 1

    def search(self, value):    ## O(n) time complexity
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
            if current == self.head:
                break
        return False

    def get(self, index): ## O(n) time complexity
        if index < -1 or index >= self.length:
            return
        if index == -1:
            return self.tail
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set(self, index, value):    # O(n) time complexity
        target_node = self.get(index)
        if target_node:
            target_node.value = value
            return True
        return False

    def popfirst(self): ## O(1) time complexity
        if self.head is None:
            return 
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            pop_node = self.head
            self.head = pop_node.next
            self.tail.next = self.head
            pop_node.next = None
        self.length -= 1
        return pop_node

    def pop(self):  ## O(n) time complexity
        if self.tail is None:
            return
        pop_node = self.tail
        if self.length == 1:            
            self.head = None
            self.tail = None
        else:
            prev_node = self.head
            while prev_node.next is not self.tail:
                prev_node = prev_node.next
            self.tail = prev_node
            prev_node.next = self.head
        pop_node.next = None
        self.length -= 1
        return pop_node

    def remove(self, index):    ## O(n) time complexity
        if index < 0 or index >= self.length:
            return
        elif index == 0:
            return self.popfirst()
        elif index == self.length-1:
            return self.pop()
        else:
            prev_node = self.get(index-1)
            del_node = prev_node.next
            prev_node.next = del_node.next
            del_node.next = None
        return del_node
    
    def delete_all(self): ## O(1) time complexity
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0

    def delete_by_value(self, value):
        # TODO
        if self.length == 0:
            return False
        elif value == self.head.value:
            del_node = self.head
            self.head = del_node.next
            self.tail = self.head
            self.length -= 1
            return True
        else:
            prev_node = self.head
            while prev_node.next is not None:
                if prev_node.next.value == value:
                    del_node = prev_node.next
                    prev_node.next = del_node.next
                    del_node.next = None
                    self.length -= 1
                    if del_node == self.tail:
                        prev_node.next = self.head
                        self.tail = prev_node
                    return True
                else:
                    prev_node = prev_node.next
                
                if prev_node == self.head:
                    break
            
            return False  


cs_linked_list = CSLinkedList()
cs_linked_list.append(0)
cs_linked_list.append(10)
cs_linked_list.append(20)
cs_linked_list.append(30)
cs_linked_list.prepend(-10)
cs_linked_list.prepend(-20)

print(cs_linked_list)
# cs_linked_list.insert(0, 5)
# cs_linked_list.insert(1, 6)
# print(cs_linked_list.get(-1).value)
#print(cs_linked_list.popfirst().value)
print(cs_linked_list.delete_by_value(30))
cs_linked_list.print_linked_list()
#print(cs_linked_list)



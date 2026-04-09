class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        temp = self.head
        result = []
        while True:
            result.append(temp.data)
            print(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        return " -> ".join(map(str, result)) + " -> (back to head)"

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node


    def insert_into_sorted(self, data):
        # TODO
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return True
        temp = self.head
        if temp.data >= data:
            self.prepend(data)
            return True
        while temp is not None:
            print(temp.data, temp.next.data)
            if temp.next == self.head:
                    self.append(data)

                    return True
            elif data <= temp.next.data:
                new_node.next = temp.next
                temp.next = new_node
                return True
            temp = temp.next
        return False



cs_list = CircularLinkedList()
cs_list.append(1)
cs_list.append(3)
cs_list.append(5)
print(cs_list.insert_into_sorted(0))
print(cs_list.insert_into_sorted(7))
print(cs_list)
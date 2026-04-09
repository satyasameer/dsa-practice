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
            # print(temp.data)
            temp = temp.next
            if temp == self.head:
                break
        return " -> ".join(map(str, result)) + " -> (back to head)"

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def count_nodes(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    def delete_node(self, key):
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = cur.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur.data == key:
                    prev.next = cur.next
                    cur = cur.next

    def josephus_circle(self, step):
        if self.head is None:
            return None
        temp = self.head
        # TODO
        while temp.next != temp:
            for _ in range(step-1):
                temp = temp.next
            #print("removing: ", temp.data)
            self.delete_node(temp.data)
            temp = temp.next
            #print(self, "---", temp.data)

        return f"Last person left standing: {temp.data}"


people = CircularLinkedList()
people.append(1)
people.append(2)
people.append(3)
people.append(4)
people.append(5)
# people.append(6)
print(people)
print(people.josephus_circle(2))

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop condition for circular list
                break
            result += ' -> '
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1


    def split_list(self): ## O(n) time complexity / O(n) space complexity
            # TODO
            if self.head is None:
                return None, None
            slow = self.head
            fast = self.head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
                
                if fast.next == self.head or fast.next.next == self.head:
                    break
            #print(slow.value, fast.value)
            first_list = CSLinkedList()
            temp = self.head
            while first_list:
                first_list.append(temp.value)
                temp = temp.next
                if temp == slow:
                    break
            if self.length % 2 != 0:
                first_list.append(temp.value)
                temp = temp.next
            second_list = CSLinkedList()
            while second_list:
                second_list.append(temp.value)
                temp = temp.next
                if temp == self.head:
                    break
            # print(first_list.head, first_list.tail, first_list.tail.next)
            # print(second_list.head, second_list.tail, second_list.tail.next)
            print(first_list)
            print(second_list)
            
            return first_list, second_list

    def split_list_better(self):  ## O(n) time complexity / O(1) space complexity
        if self.length == 0:
            return None, None
        slow = self.head
        fast = self.head
        while True:
            slow = slow.next
            fast = fast.next.next

            if fast.next is self.head or fast.next.next is self.head:
                break
        if fast.next.next == self.head:
            fast = fast.next

        # print("fast: ", fast, "slow: ", slow)

        head1 = self.head
        head2 = slow.next

        fast.next = slow.next
        slow.next = self.head

        first_list = CSLinkedList()
        first_list.head = head1
        first_list.tail = slow
        

        second_list = CSLinkedList()
        second_list.head = head2
        second_list.tail = fast

        # print(head1, head2)
        # print(first_list)
        # print(second_list)
        return first_list, second_list

cs_list = CSLinkedList()
cs_list.append(1)
cs_list.append(2)
cs_list.append(3)
cs_list.append(4)
cs_list.append(5)
cs_list.append(6)
cs_list.append(7)
cs_list.append(8)
print(cs_list)
print(cs_list.split_list_better())
# [print(obj) for obj in cs_list.split_list()]
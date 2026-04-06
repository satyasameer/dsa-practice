
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def __str__(self) -> str:
        current = self.dummy.next
        result = []
        while current:
            result.append(str(current.val))
            current = current.next
        return "->".join(result)
            
    def mergeTwoLists(self, l1, l2):  ## O(n+m) time complexity
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        self.dummy = ListNode(0)
        current = self.dummy
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
        current.next = l1 if l1 else l2
        return self.dummy.next

            


new_solution = Solution()
l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l7 = ListNode(7)
l8 = ListNode(8) 
l1.next = l3
l3.next = l5
l5.next = l7
l2.next = l4
l4.next = l6
l6.next = l8

new_solution.mergeTwoLists(l1, l2)
print(new_solution)

"""
1->3->5->6->7
2->4->6->8

1->2->
"""                
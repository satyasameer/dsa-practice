# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find mid point
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None
        #print("slow ->", slow.val)
        #print("second ->", second.val)

        # reverse second half
        curr = second
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second = prev
        
        #first_print = head
        #second_print = second
        #hile first_print:
        #    print(first_print.val, end=" ")
        #    first_print = first_print.next
        #print("")
        #while second_print:
        #    print(second_print.val, end=" ")
        #    second_print = second_print.next
        
        # merge both halves for the result
        first = head
        while second:
            first_next = first.next
            second_next = second.next
            first.next = second
            second.next = first_next
            second = second_next
            first = first_next
        
        
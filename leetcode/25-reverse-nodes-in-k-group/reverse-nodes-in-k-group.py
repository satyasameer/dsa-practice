# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        groupEnd = dummy
        while groupEnd:
            groupStart = groupPrev.next
            groupEnd = groupPrev
            for _ in range(k):
                groupEnd = groupEnd.next
                if not groupEnd:
                    return dummy.next
            # print("GS: ", groupStart.val, "GE: ", groupEnd.val, "GP: ", groupPrev.val)
            nextGroup = groupEnd.next
            prev = nextGroup
            curr = groupStart
            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            groupPrev.next = groupEnd
            groupPrev = groupStart
            # print_pointer = dummy.next
            # while print_pointer:
            #    print(print_pointer.val, end=" ")
            #    print_pointer = print_pointer.next
            # print("")
        return dummy.next



        
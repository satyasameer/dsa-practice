# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        dummy = ListNode(-1)
        dummy.next = head
        slow = head
        fast = head
        prev = dummy
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # print(slow, prev)
        prev.next = slow.next
        slow.next = None
        return dummy.next
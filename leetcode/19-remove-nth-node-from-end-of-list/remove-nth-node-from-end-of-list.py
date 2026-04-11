# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return
        dummy = ListNode(0, head)
        slow = dummy
        fast = dummy
        for _ in range(n+1):
            fast = fast.next
        print(slow, fast)
        while fast:
            slow = slow.next
            fast = fast.next
        del_node = slow.next
        slow.next = del_node.next
        del_node.next = None
        return dummy.next



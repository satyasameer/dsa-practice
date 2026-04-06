class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = None

class Solution:
    def middleNode(self, head):
        if head is None:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow
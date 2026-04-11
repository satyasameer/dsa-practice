# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None:
            return head
        dummy = ListNode(-1, head)
        oddHead = head
        evenHead = head.next
        head1 = oddHead
        head2 = evenHead
        while evenHead and evenHead.next:
            oddHead.next = evenHead.next
            oddHead = oddHead.next
            evenHead.next = oddHead.next
            evenHead = evenHead.next
        oddHead.next = head2
        #print(head1)
        #print(head2)
        return head1

        
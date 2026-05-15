# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        heap = []
        counter = 0
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, counter, head))
                counter += 1
        
        while heap:
            _,_,smallest_node = heapq.heappop(heap)
            current.next = smallest_node
            current = current.next
            if smallest_node.next:
                heapq.heappush(heap, (smallest_node.next.val, counter, smallest_node.next))
                counter += 1
        
        return dummy.next

        
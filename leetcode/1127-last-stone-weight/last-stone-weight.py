import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-weight for weight in stones]
        # print(heap)
        heapq.heapify(heap)
        # print(heap)
        while len(heap) > 1 :
            y = heapq.heappop(heap)
            x = heapq.heappop(heap)
            if y != x:
                heapq.heappush(heap, -abs(y-x))
        
        return -heap[0] if heap else 0

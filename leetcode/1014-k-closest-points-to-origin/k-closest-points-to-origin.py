class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        n = len(points)
        for i in range(n):
            distance = points[i][0]**2 + points[i][1]**2
            if i < k:
                heapq.heappush(heap, (-distance, points[i]))
            else:
                if distance < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-distance, points[i]))
            # print(distance, points[i], heap)
        return [point for _,point in heap]
from math import ceil

class Solution:
    def canFinish(self, piles, h, speed):
        total_hours = 0
        for num in piles:
            total_hours += ceil(num/speed)
        return total_hours <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        # for i in range(max(piles)):
        #     print(i, self.canFinish(piles, h , i))
        while left < right:
            mid = (left+right)//2
            # print(mid, self.canFinish(piles, h , mid))
            if self.canFinish(piles, h, mid):
                right = mid
            else:
                left = mid + 1
        
        return left

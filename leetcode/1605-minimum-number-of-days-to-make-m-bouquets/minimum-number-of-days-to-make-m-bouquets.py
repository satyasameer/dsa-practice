class Solution:
    def canMakeBouquets(self, bloomDay: List[int], m: int, k: int, days: int) -> bool:
        bouquets_made = 0
        flowers_in_streak = 0
        for day in bloomDay:
            if day <= days:
                flowers_in_streak += 1
                if flowers_in_streak == k:
                    bouquets_made += 1
                    flowers_in_streak = 0
            else:
                flowers_in_streak = 0
        
        return bouquets_made >= m

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        left = min(bloomDay)
        right = max(bloomDay)
        n = len(bloomDay)
        if m*k > n:
            return -1
        
        while left < right:
            mid = (left+right)//2
            if self.canMakeBouquets(bloomDay, m, k, mid):
                right = mid
            else:
                left = mid+1
        return left

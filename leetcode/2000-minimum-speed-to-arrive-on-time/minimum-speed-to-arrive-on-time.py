class Solution:
    def canReachDest(self, dist: List[int], hour: float, speed: int) -> bool:
        total_time = 0
        for d in dist[:-1]:
            total_time += (d+speed-1)//speed
            # print(total_time, d, "train at speed ", speed)
        return (total_time + dist[-1]/speed) <= hour
        
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        if hour <= len(dist)-1:
            return -1
        lower = 1
        upper = 10**7
        while lower < upper:
            mid = (lower+upper)//2
            if self.canReachDest(dist, hour, mid):
                upper = mid
            else:
                lower = mid+1
        
        return lower
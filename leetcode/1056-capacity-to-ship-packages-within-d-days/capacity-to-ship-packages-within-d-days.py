class Solution:
    def canShip(self, weights: List[int], days: int, capacity: int) -> bool:
        current_load = 0
        days_to_ship = 1
        for weight in weights:
            current_load += weight
            if current_load > capacity:
                days_to_ship += 1 
                current_load = weight
            # print(current_load, days_to_ship, capacity, days)

        return days_to_ship <= days 


    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left = max(weights)
        right = sum(weights)
        while left < right:
            mid = (left+right)//2
            # print(left, right, mid, "--", self.canShip(weights, days, mid))
            if self.canShip(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left
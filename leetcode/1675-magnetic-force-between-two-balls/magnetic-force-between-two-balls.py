class Solution:
    def canPlace(self, position: List[int], m: int, distance: int) -> bool:
        last_placed_position = position[0]
        balls_placed = 1
        for pos in position[1:]:
            # print(last_placed_position, balls_placed, pos)
            if pos - last_placed_position >= distance:
                last_placed_position = pos
                balls_placed += 1
        # print(last_placed_position, balls_placed, pos)
        return balls_placed >= m




    def maxDistance(self, position: List[int], m: int) -> int:
        left = 1
        right = max(position) - min(position)
        position.sort()
        while left < right:
            mid = (left+right+1)//2
            # print(left, right, mid, "--")
            if self.canPlace(position, m, mid):
                left = mid
            else:
                right = mid-1
        return left

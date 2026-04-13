class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        min_value = float('inf')
        for i,num in enumerate(nums):
            if num == target:
                value = abs(i - start)
                if value < min_value:
                    min_value = value
        return min_value

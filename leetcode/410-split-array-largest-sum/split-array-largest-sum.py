class Solution:
    def canSplit(self, nums: List[int], k: int, possible_sum: int) -> bool:
        current_sum = 0
        subarray_count = 0
        for num in nums:
            current_sum += num
            if current_sum > possible_sum:
                subarray_count += 1
                current_sum = num
        return subarray_count+1 <= k

    def splitArray(self, nums: List[int], k: int) -> int:
        lower = max(nums)
        upper = sum(nums)
        while lower < upper:
            mid = (lower+upper)//2
            if self.canSplit(nums, k, mid):
                upper = mid
            else:
                lower = mid+1
        return lower
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid+1
        if nums[left] >= target:
            return left
        else:
            return right + 1

        # for i in range(len(nums)):
        #     if nums[i]>=target:
        #         return i
        # return i+1 

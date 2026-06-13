from math import ceil

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if nums == []:
            return [-1,-1]
        n = len(nums)
        left = 0
        right = n - 1
        result = [-1,-1]
        while left < right:
            mid = (left+right)//2
            # print(left, right, mid)
            if nums[mid] >= target:
                right = mid
            else:
                left = mid+1
        if nums[left] == target:
            result[0]=left

        left = 0
        right = n - 1
        while left < right:
            mid = ceil((left+right)/2)
            if nums[mid] <= target:
                left = mid
            else:
                right = mid-1
        if nums[left] == target:
            result[1]=left

        return result



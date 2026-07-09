class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        sorted_nums = [[v,i] for i,v in enumerate(nums)]
        sorted_nums = sorted(sorted_nums, key=lambda x: x[0])
        print(sorted_nums)
        while left < right:
            total = sorted_nums[left][0] + sorted_nums[right][0]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                print(total, left, right)
                return [sorted_nums[left][1], sorted_nums[right][1]]
        # seen = {}
        # for i,num in enumerate(nums):
        #     needed = target - num
        #     if needed in seen:
        #         return [seen[needed], i]    
        #     seen[num] = i
            
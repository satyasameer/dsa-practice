class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = len(nums)
        left_prefix_sum = [0] * l
        prefix_sum = 0
        for i in range(l):
            left_prefix_sum[i] = prefix_sum
            prefix_sum += nums[i]
        
        # print(left_prefix_sum)
        prefix_sum = 0
        right_prefix_sum = [0] * l
        for i in range(l-1,-1,-1):
            right_prefix_sum[i] = prefix_sum
            prefix_sum += nums[i]
        
        for i in range(l):
            if left_prefix_sum[i] == right_prefix_sum[i]:
                return i
        return -1
            

            

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        freq = {0:-1}
        prefixSum = 0
        for i,num in enumerate(nums):
            prefixSum += num
            remainder = prefixSum % k
            if remainder in freq and i-freq[remainder] >=2:
                return True
            if remainder not in freq:
                freq[remainder] = i
            
        return False

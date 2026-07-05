class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = {0:1}
        prefixSum = 0
        count = 0
        for i,num in enumerate(nums):
            prefixSum += num
            need = prefixSum-goal
            if need in freq:
                count += freq[need]
            freq[prefixSum] = freq.get(prefixSum,0) + 1
        return count

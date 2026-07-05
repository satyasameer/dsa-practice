class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        prefixSum = 0
        count = 0
        for i, num in enumerate(nums):
            prefixSum += num
            remainder = prefixSum % k 
            if remainder in freq:
                count += freq[remainder]
            freq[remainder] = freq.get(remainder, 0) + 1    
            # print(prefixSum, remainder, freq, count)
        
        return count
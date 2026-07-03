class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        freq = {0:1}
        for i, num in enumerate(nums):
            prefix_sum += num
            need = prefix_sum - k
            count += freq.get(need,0)
            freq[prefix_sum] = freq.get(prefix_sum, 0) + 1
            # print(freq, prefix_sum, count)
        return count
        
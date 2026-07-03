class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix_sum = 0
        indices_sum = {0:1}
        for i, num in enumerate(nums):
            prefix_sum += num
            need = prefix_sum - k
            if need in indices_sum:
                count += indices_sum[need]
            indices_sum[prefix_sum] = indices_sum.get(prefix_sum, 0) + 1
            # print(indices_sum, prefix_sum, count)
        return count
        
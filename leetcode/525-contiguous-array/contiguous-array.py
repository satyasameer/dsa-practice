class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefixSum = {0:-1}
        maxLength = 0
        totalSum = 0
        for i, num in enumerate(nums):
            if num == 0:
                totalSum -= 1
            else:
                totalSum += 1
            if totalSum not in prefixSum:
                prefixSum[totalSum] = i
            maxLength = max(maxLength, i - prefixSum[totalSum])
            # print(totalSum, maxLength)
        return maxLength


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = len(nums)
        for i in range(len(nums)):
            if nums[i] == val:
                nums[i] = -nums[i]
                k -= 1
        nums.sort(reverse=True)
        return k
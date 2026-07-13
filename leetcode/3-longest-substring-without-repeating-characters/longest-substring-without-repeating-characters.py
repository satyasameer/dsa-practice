class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxLength = 0
        charSet = set()
        for i,char in enumerate(s):
            while char in charSet:
                charSet.remove(s[left])
                left += 1
            charSet.add(char)
            maxLength = max(maxLength, i-left+1)
            # print(left, i, charSet, maxLength, s[left:i+1])
        
        return maxLength
            
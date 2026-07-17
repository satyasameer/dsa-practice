class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        target = [0] * 26
        window = [0] * 26
        result = []
        for char in p:
            target[ord(char)-ord('a')] += 1
        
        # print(target)
        k = len(p)
        left = 0
        for i in range(k):
            window[ord(s[i])-ord('a')] += 1
        # print(window)
        if target == window:
            result.append(left)
        for i in range(k,len(s)):
            window[ord(s[left])-ord('a')] -= 1
            left += 1
            window[ord(s[i]) - ord('a')] += 1
            if target == window:
                result.append(left)

        return result
            
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charMapT = {}
        charMapS = {}
        for char in t:
            charMapT[char] = charMapT.get(char, 0) + 1
        # print(charMapT)
        left = 0
        matched = 0
        required = len(charMapT)
        minLength = float('inf')
        answer = []
        for right in range(len(s)):
            charMapS[s[right]] = charMapS.get(s[right], 0) + 1
            if charMapS[s[right]] == charMapT.get(s[right], 0):
                matched += 1
            while matched == required:
                if right - left + 1 < minLength:
                    answer = [left, right]
                    minLength = right - left + 1
                charMapS[s[left]] -= 1
                if charMapS[s[left]] < charMapT.get(s[left], 0):
                    matched -= 1
                if charMapS[s[left]] == 0:
                    del charMapS[s[left]]
                left += 1
            # print("window", s[left:right+1], charMapS)
        return s[answer[0]:answer[1]+1] if minLength != float('inf') else ""
                




class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_s_count = {}
        char_t_count = {}
        for char in s:
            char_s_count[char] = char_s_count.get(char, 0) + 1
        for char in t:
            char_t_count[char] = char_t_count.get(char, 0) + 1
        return char_s_count == char_t_count 
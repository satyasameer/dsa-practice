class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count_chars_m = {}
        count_chars_r = {}
        for char in ransomNote:
            count_chars_r[char] = count_chars_r.get(char, 0) + 1
        for char in magazine:
            count_chars_m[char] = count_chars_m.get(char, 0) + 1
        # return all(count_chars_m.get(char,-1) >= count_chars_r.get(char) for char in count_chars_r)
        for char in count_chars_r:
            if count_chars_m.get(char,-1) < count_chars_r.get(char):
                return False
        return True
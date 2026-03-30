class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            if s[i:i+2] == 'IV' or s[i:i+2] == 'IX':
                result -= 1
            elif s[i] == 'I':
               result += 1
            elif s[i] == 'V':
                result += 5
            elif s[i:i+2] == 'XL' or s[i:i+2] == 'XC':
                result -= 10
            elif s[i] == 'X':
                result += 10
            elif s[i] == 'L':
                result += 50
            elif s[i:i+2] == 'CD' or s[i:i+2] == 'CM':
                result -= 100
            elif s[i] == 'C':
                result += 100
            elif s[i] == 'D':
                result += 500
            elif s[i] == 'M':
                result += 1000
            #print(f"result: {result}")
        return result

        
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_lst = list(str(x))
        #print(x_lst,list(reversed(x_lst)))
        return x_lst == list(reversed(x_lst))
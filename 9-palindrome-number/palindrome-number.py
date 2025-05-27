class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            return False
        else:
            b=str(x)[::-1]
            return x==int(b)
        
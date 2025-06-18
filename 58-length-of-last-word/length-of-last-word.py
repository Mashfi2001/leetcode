class Solution(object):
    def lengthOfLastWord(self, s):
        a=s.split(' ')
        while '' in a:
            a.remove('')
        return len(a[len(a)-1])
        
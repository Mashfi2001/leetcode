class Solution(object):
    def romanToInt(self, s):
        value_dict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        sums=0
        for i in range(len(s)):
            if i+1>=len(s):
                sums+=value_dict[s[i]]
            elif value_dict[s[i+1]]>value_dict[s[i]]:
                sums-=value_dict[s[i]]
            else:
                sums+=value_dict[s[i]]
        return sums

        
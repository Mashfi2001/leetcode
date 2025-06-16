class Solution(object):
    def plusOne(self, digits):
        num = ""
        for i in digits:
            num+=str(i)
        num=int(num)+1
        result=[]
        for j in str(num):
            result.append(int(j))
        return result
        
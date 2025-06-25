class Solution(object):
    def addBinary(self, a, b):
        count=0
        num1=0
        add=len(a)-1
        while count<len(a):
            num1+=int(a[count])*2**add
            add-=1
            count+=1
        count=0
        add=len(b)-1
        num2=0
        while count<len(b):
            num2+=int(b[count])*2**add
            add-=1
            count+=1
        num=num1+num2
        if num == 0:
            return '0'
        result=''
        while num!=1:
            result=str(num%2) + result
            num//=2
        result='1'+result
        return result
            
            
            
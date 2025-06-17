class Solution(object):
    def isValid(self, s):
        a=[]
        for i in s:
            if i == ')' and len(a) !=0 :
                if a[len(a)-1] == '(':
                    a.pop(len(a)-1)
                else:
                    return False
            elif i == '}'and len(a) !=0 :
                if a[len(a)-1] == '{':
                    a.pop(len(a)-1)
                else:
                    return False
            elif i == ']'and len(a) !=0 :
                if a[len(a)-1] == '[':
                    a.pop(len(a)-1)
                else:
                    return False
            elif i in ('(','{','['):
                a.append(i)
            else:
                return False
        if len(a) == 0:
            return True
        else:
            return False
        
        
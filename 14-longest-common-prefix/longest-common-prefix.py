class Solution(object):
    def longestCommonPrefix(self, strs):
        checker=strs[0]
        if checker == "" or len(strs) == 1 :
            return(checker)
        if strs[1] == "":
            return("")
        for i in range(1,len(strs),1):
            if checker == "":
                return ""
            if checker[0] == strs[1][0]:
                for j in range(len(checker)):
                    if j>len(strs[i])-1:
                        checker=checker[:j]
                        break
                    elif checker[j] != strs[i][j]:
                        checker=checker[:j]
                        break
            else:
                return""
        return checker
                    
                        

                            

                
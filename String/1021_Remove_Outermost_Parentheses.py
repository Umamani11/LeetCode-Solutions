class Solution(object):
    def removeOuterParentheses(self, s):
       valid=0
       start=0
       lis=[]
       for i,char in enumerate(s):
            if char=="(":
                valid+=1
            else:
                valid-=1
            if valid==0:
                lis.append(s[start+1:i])
                start=i+1
       return "".join(lis)
        
class Solution(object):
    def isValid(self, s):
        stack=[]
        pairs={
            '(':')',
            '[':']',
            '{':'}'
        }
        for ch in s:
            if ch in pairs.keys():
                stack.append(ch)
            else:
                if not stack or  pairs[stack[-1]]!=ch:
                    return False
                stack.pop()
        return len(stack)==0
      


   
        #       x=[]
        # for i in range(len(s)):
        #     if s[i]=='{' or s[i]=='(' or s[i]=='[':
        #         x.append(s[i])
        #     else:
        #         if len(x)==0:
        #             return False
        #         last=x.pop()
        #         if s[i]==')' and last!='(':
        #             return False
        #         if s[i]=='}' and last!='{':
        #             return False
        #         if s[i]==']' and last!='[':
        #             return False
        
        # if len(x)!=0:
        #     return False
        # else:
        #     return True
  
        
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
         return False
        temp=x
        rev=0
        while x!=0:
            digit=x%10
            rev=rev*10+digit
            x=x//10
        if rev == temp:
            return True
        return False

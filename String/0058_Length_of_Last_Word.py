class Solution(object):
    def lengthOfLastWord(self, s):
       str=s.split()
       return len(str[-1])
        
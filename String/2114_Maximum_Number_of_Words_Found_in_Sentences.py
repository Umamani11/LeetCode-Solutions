class Solution(object):
    def mostWordsFound(self, sentences):
        maxcount=0
        for s in sentences:
            count=len(s.split())
            maxcount=max(maxcount,count)
        return maxcount

        
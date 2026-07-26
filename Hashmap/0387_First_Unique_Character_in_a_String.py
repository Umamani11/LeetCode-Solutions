class Solution(object):
    def firstUniqChar(self, s):
        freq={}
        for ch in s:
            freq[ch]=freq.get(ch,0)+1
        for index,character in  enumerate(s):
            if freq[character]==1:
                return index
        return -1

        
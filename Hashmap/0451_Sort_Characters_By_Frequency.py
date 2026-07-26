class Solution(object):
    def frequencySort(self, s):
      freq={}
      for i in s:
        if i in freq:
            freq[i]+=1
        else:
            freq[i]=1
      sortedhash=sorted(freq.items(),key=lambda x:x[1],reverse=True)
      result=""
      for keys,values in sortedhash:
        result +=keys*values
      return result
        
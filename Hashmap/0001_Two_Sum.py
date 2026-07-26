class Solution(object):
    def twoSum(self, nums, target):
        hashma={}
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in hashma:
                return[hashma[complement],i]
            hashma[nums[i]]=i
        

                    
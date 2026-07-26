from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums, k):
        return self.at_most(nums, k) - self.at_most(nums, k - 1)

    def at_most(self, nums, k):
        left = 0
        count = 0
        freq = defaultdict(int)

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while len(freq) > k:
                freq[nums[left]] -= 1

                if freq[nums[left]] == 0:
                    del freq[nums[left]]

                left += 1

            count += right - left + 1

        return count
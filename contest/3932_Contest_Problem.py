class Solution(object):
    def countKthRoots(self, l, r, k):

        def kth_root_floor(n):

            low = 0
            high = n

            while low <= high:

                mid = (low + high) // 2

                if mid ** k <= n:
                    low = mid + 1
                else:
                    high = mid - 1

            return high

        right = kth_root_floor(r)
        left = kth_root_floor(l - 1)

        return right - left
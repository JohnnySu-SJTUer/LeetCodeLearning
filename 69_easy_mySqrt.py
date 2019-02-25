class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        :二分法查找
        """
        l, r = 0, x
        while l <= r:
            mid = l + (r - l) // 2
            if mid ** 2 <= x < (mid + 1) ** 2:
                return mid
            elif x < mid ** 2:
                r = mid
            else:
                l = mid + 1

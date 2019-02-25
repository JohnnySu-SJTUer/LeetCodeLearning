class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        :当有n个台阶时，可供选择的走法可以分两类：1，先跨一阶再跨完剩下n-1阶；2，先跨2阶再跨完剩下n-2阶         :所以n阶的不同走法的数目是n-1阶和n-2阶的走法数的和。
        """
        if n==0 or n == 1 or n == 2:
            return n
        a=[]
        a.append(1)
        a.append(1)
        for i in range(2,n+1):
            a.append(a[i-1]+a[-2])
        return a[n]

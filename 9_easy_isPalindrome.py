class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_str = str(x) #int to str
        i = 0
        j = len(x_str)-1
        if j == 0:
            return True
        while (x_str[i] == x_str[j]) and (i <= j):
            i = i + 1
            j = j - 1
        if i < j:
            return False
        else:
            return True
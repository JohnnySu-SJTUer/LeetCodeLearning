class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        flag = 0 #record the negative
        y = 0
        if x<0:
            flag = 1
            x = -x
        while x!=0:
            unitsDigit = x%10
            y= y*10+unitsDigit
            x =int(x/10)
        if flag==1:
            y = -y
        if y<-2147483648 or y>2147483647:
            return 0
        return y
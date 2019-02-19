class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l_left = ['(','[','{']
        l_right = [')',']','}']
        l_temp = []
        for char in s:
            if char in l_left:
                l_temp.append(char)
            elif char in l_right:
                if l_temp!=[] and l_right.index(char)==l_left.index(l_temp[-1]):
                    l_temp.pop()
                else:
                    return False
            else:
                return False
        return l_temp==[]
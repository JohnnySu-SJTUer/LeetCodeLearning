class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        s = str.strip()
        syb = 1
        ptr = 0
        res = 0
        if len(s) == 0:
            return 0
        if s[0] == '-':
            syb = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]
        if len(s) == 0:
            return 0
        while s[ptr].isnumeric():
            res = res * 10 + int(s[ptr])
            ptr += 1
            if ptr >= len(s):
                break
        res = res * syb
        if res > 2147483647:
            res =  2147483647
        elif res < -2147483648:
            res = -2147483648
        return res

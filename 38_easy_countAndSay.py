class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = '1'
        for _ in range(n - 1):
            temp = res[0]
            count = 0
            resTemp = ''
            for c in res:
                if temp != c:
                    resTemp += str(count) + temp
                    temp = c
                    count = 1
                else:
                    count += 1
            resTemp += str(count) + temp
            res = resTemp
        return res

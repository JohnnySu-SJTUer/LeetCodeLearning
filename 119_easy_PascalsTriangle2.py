class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        # 52 ms, faster than 95.08%
        tempRowIndex = rowIndex
        if not rowIndex: return [1]
        res = [[1]]
        # rowIndex -= 1
        while rowIndex:
            res.append([1]+[x+y for x,y in zip(res[-1][:-1],res[-1][1:])]+[1])
            rowIndex -= 1
        return res[tempRowIndex]

if __name__=='__main__':
    s = Solution
    res = s.getRow(s,3)
    print(res)
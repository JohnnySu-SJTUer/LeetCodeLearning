class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        # 76 ms, faster than 11.16%
        # if numRows==0:
        #     return []
        # resList = [[1]]
        # for i in range(1,numRows):
        #     resList.append([1])
        #     for j in range(1,i+1):
        #         if j == i:
        #             resList[i].append(1)
        #         else:
        #             resList[i].append(resList[i-1][j-1]+resList[i-1][j])
        #
        # return resList

        # 52 ms, faster than 95.25%
        if not numRows: return []
        res = [[1]]
        numRows -= 1
        while numRows:
            res.append([1]+[x+y for x,y in zip(res[-1][:-1],res[-1][1:])]+[1])
            numRows -= 1
        return res

if __name__=='__main__':
    s = Solution
    res = s.generate(s,5)
    print(res)
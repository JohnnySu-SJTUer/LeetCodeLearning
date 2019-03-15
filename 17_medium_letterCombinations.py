class Solution:
    def letterCombinations(self, digits: str):
        if not digits:
            return []
        self.DigitDict = [' ', '1', "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        res = ['']
        for d in digits:
            res = self.letterCombBT(int(d), res)
        return res

    def letterCombBT(self, digit, oldStrList):
        return [dstr + i for i in self.DigitDict[digit] for dstr in oldStrList]

if __name__=='__main__':

    s = Solution()
    print(s.letterCombinations("23"))
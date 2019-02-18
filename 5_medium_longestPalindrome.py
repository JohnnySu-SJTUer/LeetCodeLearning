class Solution:
    # def listReverse(self, inList):
    #     res = []
    #     for i in range(len(inList)):
    #         res.append(inList[-i-1])
    #     return res
    # def longestPalindrome(self, s):
    #     """
    #     :type s: str
    #     :rtype: str
    #     """
    #     longest = 0
    #     stringList = list(s)
    #     if len(stringList)==1:
    #         return s
    #     charList = []
    #     for i in range(len(s)):
    #         for j in range(0,i+1):
    #             print(f'{stringList[i-j:i+1]}:{self.listReverse(self, stringList[i+1:i+j+2])}')
    #             if stringList[i-j:i+1]==self.listReverse(self, stringList[i+1:i+j+2]):
    #                 if 2*(j+1)>longest:
    #                     longest = 2*(j+1)
    #                     charList = stringList[i-j:i+j+2]
    #             print(f'{stringList[i-j:i+1]}:{self.listReverse(self, stringList[i+2:i+j+3])}')
    #             if stringList[i-j:i+1]==self.listReverse(self, stringList[i+2:i+j+3]):
    #                 if 2*(j+1)+1>longest:
    #                     longest = 2*(j+1)+1
    #                     charList = stringList[i-j:i+j+3]
    #             print(charList)
    #     if longest:
    #         return "".join(charList)
    #     else:
    #         return ""

    def longestPalindrome(self, s):
        res = ""
        for i in range(len(s)):
            # odd case, like "aba"
            tmp = self.palindrome(self, s, i, i)
            if len(tmp) > len(res):
                res = tmp
            # even case, like "abba"
            tmp = self.palindrome(self, s, i, i + 1)
            if len(tmp) > len(res):
                res = tmp
        return res

    # get the longest palindrome, l, r are the middle indexes
    # from inner to outer
    def palindrome(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]


if __name__=='__main__':
    string = "baba"
    s = Solution
    print(s.longestPalindrome(s,string))

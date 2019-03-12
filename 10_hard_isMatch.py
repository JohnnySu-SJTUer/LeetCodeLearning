# import re
# class Solution:
#     def isMatch(self, s: str, p: str) -> bool:
#         return re.match('^'+p+'$',s) != None
#
# s = Solution()
# print(s.isMatch("ab",".*"))

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if len(p)==1 or p[1]!='*':
            if not s or (p[0]!='.' and p[0]!=s[0]):
                return False
            else:
                return self.isMatch(s[1:], p[1:])
        else:
            while s and (p[0]=='.' or s[0]==p[0]):
                if self.isMatch(s,p[2:]):
                    return True
                s = s[1:]

        return self.isMatch(s,p[2:])

s = Solution()
print(s.isMatch("aa","a*"))
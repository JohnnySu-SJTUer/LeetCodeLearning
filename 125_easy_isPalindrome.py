class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # if not len(s):
        #     return True
        # newStr = ''
        # for ch in s:
        #     if ch.isalnum():
        #         newStr += ch
        # lenthOfNewStr = len(newStr)
        # for i in range(lenthOfNewStr//2):
        #     if newStr[i].lower()!=newStr[lenthOfNewStr-i-1].lower():
        #         return False
        # return True
        l,r = 0,len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1
            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True

if __name__=='__main__':
    string = "112321,,1"
    s = Solution
    res = s.isPalindrome(s,string)
    print(res)
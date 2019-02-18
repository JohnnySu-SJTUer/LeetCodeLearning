class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest = 0
        stringList = list(s)
        charList = []
        for i in range(len(s)):
            currentChar = stringList[i]
            if currentChar in charList:
                charList = charList[charList.index(currentChar)+1:len(charList)]
            charList.append(currentChar)
            if len(charList)>longest:
                longest = len(charList)
        return longest

if __name__=='__main__':
    string = "abcabcbb"
    s = Solution
    print(s.lengthOfLongestSubstring(s,string))

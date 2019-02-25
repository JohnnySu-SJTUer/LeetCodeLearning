class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return str(bin(int(a,2)+int(b,2)))[2:]

if __name__ == '__main__':
    string = "11"
    string1 = "10"
    s = Solution
    print(s.addBinary(s, string,string))
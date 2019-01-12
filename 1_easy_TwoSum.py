class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dictMap = {}
        for index, value in enumerate(num):
            if target - value in dictMap:
                return dictMap[target - value], index
            dictMap[value] = index

if __name__=='__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution
    print(s.twoSum(s,nums,target)) #(0, 1)

class Solution:
    def threeSum(self, nums):
        if len(nums) < 3:
            return []
        nums.sort()
        resultList = []
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue
            d = {}
            for x in nums[i + 1:]:
                if x not in d:
                    d[-v - x] = 1
                elif [v, x, -v - x] not in resultList:
                    resultList.append([v, x, -v - x])

        return resultList

if __name__=='__main__':
    nums = [0,0,0,0]
    s = Solution
    print(s.threeSum(s,nums))

class Solution:
    # def threeSum(self, nums):
    #     if len(nums) < 3:
    #         return []
    #     nums.sort()
    #     resultList = []
    #     for i, v in enumerate(nums[:-2]):
    #         if i >= 1 and v == nums[i - 1]:
    #             continue
    #         d = {}
    #         for x in nums[i + 1:]:
    #             if x not in d:
    #                 d[-v - x] = 1
    #             elif [v, x, -v - x] not in resultList:
    #                 resultList.append([v, x, -v - x])
    #
    #     return resultList

    def threeSum(self,nums):
        if len(nums)<3:
            return []
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            target=0-nums[i]
            left,right=i+1,len(nums)-1
            while left<right:
                if nums[left]+nums[right]==target:
                    res.append([nums[i],nums[left],nums[right]])
                    while left<right and nums[left]==nums[left+1]:
                        left+=1
                    while left<right and nums[right]==nums[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif nums[left]+nums[right]<target:
                    left+=1
                else:
                    right-=1
        return res


if __name__=='__main__':
    nums = [-1, 0, 1, 2, -1, -4]
    s = Solution()
    print(s.threeSum(nums))

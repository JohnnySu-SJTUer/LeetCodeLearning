class Solution:
    def permute(self,nums):
        if not nums:
            return None
        res = []
        path=[]
        self.dfs(nums,path,res)
        return res

    def dfs(self,nums,path,res):
        if not nums:
            res.append(path)
            # return res
        else:
            for i in range(len(nums)):
                # print(nums[:i]+nums[i+1:],path+[nums[i]],res)
                self.dfs(nums[:i]+nums[i+1:],path+[nums[i]],res)

s=Solution()
print(s.permute([1,2,3]))
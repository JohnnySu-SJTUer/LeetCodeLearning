class Solution:
    def threeSumClosest(self, nums, target) -> int:
        if len(nums) < 3:
            return []
        nums.sort()
        closest=nums[0]+nums[1]+nums[2]
        diff = abs(closest-target)
        for i, v in enumerate(nums[:-2]):
            if i >= 1 and v == nums[i - 1]:
                continue
            left=i+1
            right=len(nums)-1
            while(left<right):
                sum=v+nums[left]+nums[right]
                newDiff=abs(sum-target)
                if diff>newDiff:
                    diff=newDiff
                    closest=sum
                if sum<target:
                    left+=1
                else:
                    right-=1
        return closest

if __name__=='__main__':
    nums = [-1, 2, 1, -4]
    s = Solution()
    print(s.threeSumClosest(nums,1))
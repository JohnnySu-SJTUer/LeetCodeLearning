class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        tail = 0
        for i in range(1,len(nums)):
            if nums[i] != nums[tail]:
                tail+=1
                nums[tail] = nums[i]
        return tail+1

if __name__=='__main__':
    s = Solution
    nums = [0,0,1,1,1,2,2,3,3,4]
    out = s.removeDuplicates(s, nums)
    print(out)
class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            nums.remove(val)
        return len(nums)
if __name__=='__main__':
    s = Solution
    nums = [0,1,2,2,3,0,4,2]
    out = s.removeElement(s, nums,2)
    print(out)
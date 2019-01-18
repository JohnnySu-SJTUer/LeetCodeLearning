class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # for i in range(len(nums)):
        #     if nums[i] not in nums[:i] and nums[i] not in nums[i+1:]:
        #         return nums[i]
        hashTable = {}
        for data in nums:
            try:
                hashTable.pop(data)
            except:
                hashTable[data] = 1
        return hashTable.popitem()[0]

if __name__=='__main__':
    prices = [4,1,2,1,2] #[2,2,1]
    s = Solution
    res = s.singleNumber(s,prices)
    print(res)
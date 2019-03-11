class Solution:
    def findMedianSortedArrays(self, nums1: 'List[int]', nums2: 'List[int]') -> 'float':
        l = len(nums1)+len(nums2)
        if l%2 == 1:
            return self.kth(self, nums1, nums2, l//2)
        else:
            return (self.kth(self, nums1, nums2, l//2)+self.kth(self,nums1,nums2,l//2-1))/2

    def kth(self,a,b,k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        i,j = len(a)//2,len(b)//2
        if i+j<k:
            if a[i]>b[j]:
                return self.kth(self,a,b[j+1:],k-j-1)
            else:
                return self.kth(self,a[i+1:],b,k-i-1)
        else:
            if a[i]>b[j]:
                return self.kth(self,a[:i],b,k)
            else:
                return self.kth(self,a,b[:j],k)


if __name__=='__main__':
    nums1 = [1, 3]
    nums2 = [2]
    s = Solution
    print(s.findMedianSortedArrays(s,nums1,nums2))
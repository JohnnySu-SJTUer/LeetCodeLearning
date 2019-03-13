class Solution:
    def maxArea(self, height):
        m_maxArea=0
        i,j=0,len(height)-1
        while i<j:
            h=min(height[i],height[j])
            m_maxArea=max(m_maxArea,h*(j-i))
            while height[i]<=h and i<j:
                i+=1
            while height[j]<=h and i<j:
                j-=1

        return m_maxArea

s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
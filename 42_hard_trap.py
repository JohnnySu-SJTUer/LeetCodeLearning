class Solution:
    def trapStack(self, height) -> int:
        st = []
        i,res=0,0
        while i<len(height):
            if not len(st) or height[i]<=height[st[-1]]:
                st.append(i)
                i+=1
            else:
                t=st[-1]
                st.pop()
                if not len(st):
                    continue
                res+=(min(height[i],height[st[-1]])-height[t])*(i-st[-1]-1)

        return res

    def trapLeftRight(self,height):
        res,l,r=0,0,len(height)-1
        while l<r:
            mn=min(height[l],height[r])
            if mn==height[l]:
                l+=1
                while l<r and height[l]<mn:
                    res+=mn-height[l]
                    l+=1
            else:
                r-=1
                while l<r and height[r]<mn:
                    res+=mn-height[r]
                    r-=1
        return res

s=Solution()
print(s.trapStack([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trapLeftRight([0,1,0,2,1,0,1,3,2,1,2,1]))
class Solution:
    def generateParenthesis(self, n: int):
        res=[]
        self.generateParenthesisDFS(n,n,"",res)
        return res

    def generateParenthesisDFS(self,left,right,out,res):
        if right<left:
            return
        if left==0 and right==0:
            res.append(out)
        else:
            if left>0:
                self.generateParenthesisDFS(left-1,right,out+'(',res)
            if right>0:
                self.generateParenthesisDFS(left,right-1,out+')',res)

s=Solution()
print(s.generateParenthesis(3))
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root,float('inf'),float('-inf'))

    def dfs(self,root:TreeNode,maxNum,minNum):
        if not root:
            return True
        elif root.val<=minNum or root.val>=maxNum:
            return False
        else:
            return self.dfs(root.left,root.val,minNum) and self.dfs(root.right,maxNum,root.val)

s=Solution()
print(s.isValidBST())
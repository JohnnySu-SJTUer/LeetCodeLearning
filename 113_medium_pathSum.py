# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int): # -> List[List[int]]
        if not root: return []
        res = []
        self.dfs(root,sum,res,[root.val])
        return res

    def dfs(self,root,sum,res,path):
        if not root: return
        if sum(path)==sum and root.left==None and root.right==None:
            res.append(path)
            return
        if root.left:
            self.dfs(root.left,sum,res,path+[root.left.val])
        if root.right:
            self.dfs(root.right,sum,res,path+[root.right.val])
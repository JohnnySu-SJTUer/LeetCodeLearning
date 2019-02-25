# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        :在104. Maximum Depth of Binary Tree算法BFS+Queue基础上改进
        """
        if not root:
            return []
        depth = 0
        p = [root]
        resList = [[root.val]]
        while len(p)!=0:
            depth+=1
            resList.insert(0,[])
            for i in range(len(p)):
                if p[0].left:
                    p.append(p[0].left)
                    resList[-(depth+1)].append(p[0].left.val)
                if p[0].right:
                    p.append(p[0].right)
                    resList[-(depth+1)].append(p[0].right.val)
                p.pop(0)
        return resList[1:] #删除while循环中最后插入的空'[]'

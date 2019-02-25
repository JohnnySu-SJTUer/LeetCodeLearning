# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        :BFS 使用队列的形式
        """
        if not root:
            return True
        leftQueue,rightQueue = [root.left],[root.right]
        while len(leftQueue)>0 or len(rightQueue)>0:
            left = leftQueue.pop()
            right = rightQueue.pop()
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val!=right.val:
                return False
            leftQueue.insert(0,left.right)
            leftQueue.insert(0,left.left)
            rightQueue.insert(0,right.left)
            rightQueue.insert(0,right.right)
        return len(leftQueue)==0 and len(rightQueue)==0
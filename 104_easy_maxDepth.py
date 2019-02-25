# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        :BFS+queue
        """
        if not root:
            return 0
        depth = 0
        q = [root]
        while len(q) != 0:
            depth += 1
            for i in range(len(q)):  # 寻找该层中所有子节点，插入队列
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                q.pop(0)  # 删除每一个该层节点

        return depth

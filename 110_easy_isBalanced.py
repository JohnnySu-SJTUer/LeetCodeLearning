class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.dfsHeight(root) != -1

    def dfsHeight(self,root):
        if not root:
            return 0
        leftHeight = self.dfsHeight(root.left)
        if leftHeight==-1:
            return -1
        rightHeight = self.dfsHeight(root.right)
        if rightHeight==-1:
            return -1
        if abs(leftHeight-rightHeight)>1:
            return -1
        return max(leftHeight,rightHeight)+1

def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"

if __name__=='__main__':
    s = Solution
    nums = [-10,-3,0,5,9]
    ret = s.sortedArrayToBST(s, nums)
    out = treeNodeToString(ret)
    print(out)

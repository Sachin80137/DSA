# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if(root == None):
            return 0
        def chk(a):
            if(a.left==None and a.right==None):
                return 1
            elif(a.left == None and a.right != None):
                mx = chk(a.right) +1
                return mx
            elif(a.left != None and a.right==None):
                    mx = chk(a.left)+1
                    return mx
            else:
                mx = max(chk(a.left), chk(a.right))
                mx+=1
                return mx
        return chk(root)
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorder(self,root,k,ans):
        
        if root is None:
            return

        self.inorder(root.left,k,ans)

        k[0] -= 1
        if k[0] == 0:
            print(root.val)
            ans[0] = root.val
        self.inorder(root.right,k,ans)


    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """

        cnt = 0
        k = [k]
        ans = [0]
        self.inorder(root,k,ans)
        return ans[0]
        
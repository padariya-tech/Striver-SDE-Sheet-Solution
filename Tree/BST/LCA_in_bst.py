# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from Tree.level_order_traversal import TreeNode


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # def helper(root,p,q):
        #     if root == None or root == p or root == q:
        #         return root

        #     left = helper(root.left,p,q)
        #     right = helper(root.right,p,q)

        #     if left is None:
        #         return right
        #     if right is None:
        #         return left
        #     else:
        #         return root
            
        # return helper(root,p,q)
        def helper(root,p,q):
            if root == None:
                return None
            
            if root.val > p.val and root.val > q.val:
                return helper(root.left,p,q)
            elif root.val < p.val and root.val < q.val:
                return helper(root.right,p,q)
            return root
            
        return helper(root,p,q)


        
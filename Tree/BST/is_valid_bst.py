# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
from Tree.level_order_traversal import TreeNode


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root,min_val,max_val):

            if root == None:
                return True

            if root.val >= max_val or root.val <= min_val:
                return False
            
            return helper(root.left,min_val,root.val) and helper(root.right,root.val,max_val)


        return helper(root , float('-inf'),float('inf'))
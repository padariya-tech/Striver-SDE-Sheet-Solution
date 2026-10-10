from typing import Optional

from Tree.Diameter_of_Binary_Tree import TreeNode


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        arr = [float('-inf')]

        def helper(root):
            if root is None:
                return 0
            
            left = helper(root.left)
            right = helper(root.right)

            arr[0] = max(arr[0], left + right + root.val)

            return max(left, right) + root.val
        
        helper(root)
        return arr[0]
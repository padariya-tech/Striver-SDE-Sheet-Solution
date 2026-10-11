# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def findLastRight(self,root):

        if root.right is None:
            return root

        return self.findLastRight(root.right)

    def helper(self,root):
        if root.left is None:
            return root.right

        elif root.right is None:
            return root.left

        right_child = root.right
        last_right = self.findLastRight(root.left)
        last_right.right = right_child

        return root.left
    
    def deleteNode(self, root, key):
        if root is None:
            return None

        if root.val == key:
            return self.helper(root)

        dummy = root

        while root is not None:

            if root.val > key:
                if root.left is not None and root.left.val == key:
                    root.left = self.helper(root.left)
                    break

                else:
                    root = root.left
            else:
                if root.right is not None and root.right.val == key:
                    root.right = self.helper(root.right)
                    break

                else:
                    root = root.right
        
        return dummy
        
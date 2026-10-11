# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.prev = None
        self.middle = None
        self.last = None

        def inorder(node):
            if node is None:
                return

            inorder(node.left)

            if self.prev is not None and node.val < self.prev.val:
                # first violation
                if self.first is None:
                    self.first = self.prev
                    self.middle = node
                # second violation
                else:  
                    self.last = node

            self.prev = node

            inorder(node.right)

        inorder(root)

        if self.first is not None and self.last is not None:
            self.first.val, self.last.val = self.last.val, self.first.val
        elif self.first is not None and self.middle is not None:
            self.first.val, self.middle.val = self.middle.val, self.first.val
         
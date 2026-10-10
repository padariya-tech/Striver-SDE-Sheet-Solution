from typing import Optional

from Tree.Diameter_of_Binary_Tree import TreeNode

# from the last node of the left subtree, go to the root node of that subtree
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder = []
        preorder = []
        cur = root

        while cur is not None:
            if cur.left is None:
                inorder.append(cur.val) # left element
                preorder.append(cur.val)
                cur = cur.right
            else:
                prev = cur.left
                while prev.right and prev.right != cur:
                    prev = prev.right
                
                if prev.right is None:
                    prev.right = cur
                    preorder.append(cur.val)
                    cur = cur.left
                else:
                    prev.right = None
                    inorder.append(cur.val) # root will be there
                    cur = cur.right
        
        return inorder
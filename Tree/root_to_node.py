"""
Definition of Node
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def traverse(self,root,temp,ans):
        
        # print(temp)
        if root.left is None and root.right is None:
            # print(temp)
            ans.append(temp[:])
            return
        
        if root.left:
            temp.append(root.left.data)
            self.traverse(root.left, temp, ans)
            temp.pop()  # Backtrack
            
        if root.right:
            temp.append(root.right.data)
            self.traverse(root.right, temp, ans)
            temp.pop()  # Backtrack
        
        return
    
    def paths(self, root):
        # code here
        ans = []
        self.traverse(root,[root.data],ans)
        # print(ans)
        return ans
class Solution:
    def isLeaf(self,root):
        if root.left == None and root.right == None:
            return True
        return False
    
    def addLeftBoundry(self,root,res):
        curr = root.left
        while curr:
            if not self.isLeaf(curr):
                res.append(curr.data)

            if curr.left:
                curr = curr.left
            else:
                curr = curr.right
    
    def addRightBoundry(self,root,res):
        curr = root.right
        temp = []
        while curr:
            if not self.isLeaf(curr):
                temp.append(curr.data)
            if curr.right:
                curr = curr.right
            else:
                curr = curr.left

        for i in range(len(temp)-1,-1,-1):
            res.append(temp[i])
    def addBottomBoundry(self,root,res):
        if self.isLeaf(root):
            res.append(root.data)
            return
        if root.left:
            self.addBottomBoundry(root.left,res)
        if root.right:
            self.addBottomBoundry(root.right,res)

    def boundaryTraversal(self, root):
        
        # code here
        res = []
        if not root:
            return res
        
        if not self.isLeaf(root):
            res.append(root.data)

        self.addLeftBoundry(root,res)
        self.addBottomBoundry(root,res)
        self.addRightBoundry(root,res)

        return res
    
from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None


def create_tree(arr):
    if not arr or arr[0] is None:
        return None

    root = Node(arr[0])
    q = deque([root])
    i = 1

    while q and i < len(arr):
        curr = q.popleft()

        # Create the left child
        if i < len(arr) and arr[i] is not None:
            curr.left = Node(arr[i])
            q.append(curr.left)
        i += 1

        # Create the right child
        if i < len(arr) and arr[i] is not None:
            curr.right = Node(arr[i])
            q.append(curr.right)
        i += 1

    return root


if __name__ == "__main__":

    arr = [1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, None, None]

    root = create_tree(arr)
    print(Solution().boundaryTraversal(root))
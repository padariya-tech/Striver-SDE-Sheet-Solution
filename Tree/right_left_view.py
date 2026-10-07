# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrderLeftRight(self, root):
        if root is None:
            return []
        
        q = deque()
        q.append(root)
        ans = []

        while q:
            size = len(q)
            for i in range(len(q)):
                top = q.popleft()
                if i == size - 1:
                    ans.append(top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)

        return ans

    def RecursiveLeftRight(self, root, level , st,ans):

        if root is None:
            return ans

        if len(st) == level:
            ans.append(root.val)
            st.append(root.val)

        self.RecursiveLeftRight(root.right,level+1,st,ans)
        self.RecursiveLeftRight(root.left,level+1,st,ans)

        return ans
        

def main():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.right = g
    e.left = f

    sol = Solution()
    ans = sol.levelOrderLeftRight(a) # approach 1 

    st = []
    ans = []
    ans2 = sol.RecursiveLeftRight(a,0,st,ans) # approach 2
    print(ans)
    print(ans2)


if __name__ == "__main__":
    main()

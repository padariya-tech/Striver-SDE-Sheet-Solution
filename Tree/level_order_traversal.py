# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        
        q = deque()
        q.append(root)
        ans = []

        while q:
            temp = []
            for i in range(len(q)):
                top = q.popleft()
                temp.append(top.val)
                if top.left:
                    q.append(top.left)
                if top.right:
                    q.append(top.right)

            ans.append(temp)

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
    b.left = c
    c.left = d
    a.right = e
    e.right = f
    f.right = g

    sol = Solution()
    ans = sol.levelOrder(a)
    print(ans)


if __name__ == "__main__":
    main()

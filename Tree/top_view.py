# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def topview(self, root):
        if root is None:
            return []
        
        q = deque()
        q.append([root,0]) # storing node , vertical level 
        mapp = {}  # to store the first node at each level
        while q:

            size = len(q)
            for i in range(size):

                top = q.popleft()
                val = top[0]
                idx = top[1]

                if idx not in mapp:
                    mapp[idx] = val

                if val.left:
                    q.append([val.left,idx - 1])
                if val.right:
                    q.append([val.right,idx + 1])

        return [mapp[idx].val for idx in sorted(mapp)]


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
    ans = sol.topview(a)
    print(ans)


if __name__ == "__main__":
    main()

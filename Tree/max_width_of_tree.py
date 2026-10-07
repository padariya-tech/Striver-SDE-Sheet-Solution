# Definition for a binary tree node.
from collections import deque
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def widthOfTree(self, root):
        if root is None:
            return 0
        
        q = deque()
        q.append([root,1])
        ans = float('-inf')

        while q:
            # temp = []
            min_index = 0
            # max_index = 0
            for i in range(len(q)):
                top = q.popleft()
                val = top[0]
                idx = top[1]
                ans = idx - min_index + 1
                if i == 0:
                    min_index = idx
                # temp.append(top.val)
                if val.left:
                    new_idx = (2 * idx) - min_index
                    q.append([val.left,new_idx])
                if val.right:
                    new_idx = (2 * idx + 1) - min_index
                    q.append([val.right,new_idx])
                

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
    ans = sol.widthOfTree(a)
    print(ans)


if __name__ == "__main__":
    main()

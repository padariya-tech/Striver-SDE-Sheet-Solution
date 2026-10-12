
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

        q = deque([(root, 0)])
        ans = 0

        while q:
            size = len(q)
            min_index = q[0][1]

            first = last = 0

            for i in range(size):
                node, idx = q.popleft()

                # Normalize index to avoid unnecessarily large values
                idx -= min_index

                if i == 0:
                    first = idx
                if i == size - 1:
                    last = idx

                if node.left:
                    q.append((node.left, 2 * idx))
                if node.right:
                    q.append((node.right, 2 * idx + 1))

            ans = max(ans, last - first + 1)

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
    print(sol.widthOfTree(a))


if __name__ == "__main__":
    main()

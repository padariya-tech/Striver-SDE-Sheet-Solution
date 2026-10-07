from collections import deque


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    def verticalView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        # Store:
        # node, row, column
        q = deque()
        q.append([root, 0, 0])

        # column -> list of (row, value)
        mapp = {}

        while q:

            node, row, col = q.popleft()

            if col not in mapp:
                mapp[col] = []

            mapp[col].append([row, node.val])

            if node.left:
                q.append([node.left, row + 1, col - 1])

            if node.right:
                q.append([node.right, row + 1, col + 1])

        ans = []

        # Process columns from left to right
        for col in sorted(mapp):

            # Sort by:
            # 1. row
            # 2. value
            mapp[col].sort()

            column = []

            for row, value in mapp[col]:
                column.append(value)

            ans.append(column)

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

    c.left = f
    c.right = g

    sol = Solution()

    ans = sol.verticalView(a)

    print(ans)

if __name__ == "__main__":
    main()
from collections import deque


class Solution:

    def bfs(self, root, parent_map):

        q = deque([root])
        parent_map[root] = None

        while q:
            top = q.popleft()

            if top.left:
                q.append(top.left)
                parent_map[top.left] = top

            if top.right:
                q.append(top.right)
                parent_map[top.right] = top

    from collections import deque

    def bfs_2(self, target, parent_map, k):
        q = deque([(target, 0)])
        visited = {target}
        ans = []

        while q:
            size = len(q)

            for _ in range(size):
                top, depth = q.popleft()

                if depth == k:
                    ans.append(top.val)
                    continue

                for neighbor in (top.left, top.right, parent_map[top]):
                    if neighbor is not None and neighbor not in visited:
                        visited.add(neighbor)
                        q.append((neighbor, depth + 1))

        return ans

    def distanceK(self, root, target, k):

        if root is None:
            return []

        parent_map = {}

        self.bfs(root, parent_map)

        return self.bfs_2(target, parent_map, k)
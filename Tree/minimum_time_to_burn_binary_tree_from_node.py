
from collections import deque

class Solution(object):

    def StoreParent(self, root):
        parent_map = {}
        q = deque([root])
        parent_map[root] = None
        start_node = None

        while q:
            top = q.popleft()

            if top.val == self.start:
                start_node = top

            if top.left:
                parent_map[top.left] = top
                q.append(top.left)

            if top.right:
                parent_map[top.right] = top
                q.append(top.right)

        return parent_map, start_node

    def TimeToBurn(self, start_node, parent_map):
        q = deque([start_node])
        # vis = []
        vis={start_node}
        time = -1

        while q:
            size = len(q)
            time += 1

            for _ in range(size):
                top = q.popleft()

                for neighbor in (
                    top.left,
                    top.right,
                    parent_map[top]
                ):
                    if neighbor is not None and neighbor not in vis:
                        vis.add(neighbor)
                        q.append(neighbor)

        return time

    def amountOfTime(self, root, start):
        if root is None:
            return 0

        self.start = start
        parent_map, start_node = self.StoreParent(root)

        return self.TimeToBurn(start_node, parent_map)

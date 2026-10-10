
from collections import deque

class Codec:

    def serialize(self, root):
        """Convert a binary tree into a string."""
        if not root:
            return ""

        q = deque([root])
        result = []

        while q:
            node = q.popleft()

            if node is None:
                result.append("N")
                continue

            result.append(str(node.data))
            q.append(node.left)
            q.append(node.right)

        return ",".join(result)

    def deserialize(self, data):
        """Convert a string back into a binary tree."""
        if not data:
            return None

        values = data.split(",")

        root = Node(int(values[0]))
        q = deque([root])
        i = 1

        while q and i < len(values):
            curr = q.popleft()

            # Reconstruct left child
            if values[i] != "N":
                curr.left = Node(int(values[i]))
                q.append(curr.left)
            i += 1

            # Reconstruct right child
            if i < len(values) and values[i] != "N":
                curr.right = Node(int(values[i]))
                q.append(curr.right)
            i += 1

        return root

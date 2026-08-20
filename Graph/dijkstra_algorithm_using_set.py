# Can I implement the C++ ordered-set version of Dijkstra directly using Python set?

# Not exactly. Python set doesn't maintain sorted order. '
# 'You can implement the same idea, but min() makes it O(V² + E) rather than the ordered-set version's O((V+E)log V).

class Solution:

    def dijkstra(self, adj_list):

        n = len(adj_list)

        dist = [float('inf')] * n
        dist[0] = 0

        unvisited = set(range(n))

        while unvisited:

            # Find node with minimum distance
            node = min(unvisited, key=lambda x: dist[x])

            # Remove it from unvisited
            unvisited.remove(node)

            # Relax all its edges
            for neighbor in adj_list[node]:

                v = neighbor[0]
                weight = neighbor[1]

                if dist[v] > dist[node] + weight:
                    dist[v] = dist[node] + weight

        return dist


if __name__ == "__main__":

    adj_list = [
        [[1, 4], [2, 4]],
        [[0, 4], [2, 2]],
        [[0, 4], [1, 2], [3, 3], [4, 1], [5, 6]],
        [[2, 3], [5, 2]],
        [[2, 1], [5, 3]],
        [[2, 6], [3, 2], [4, 3]]
    ]

    sol = Solution()

    answer = sol.dijkstra(adj_list)

    print(answer)
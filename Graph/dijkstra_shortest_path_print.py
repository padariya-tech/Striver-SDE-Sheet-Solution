import heapq

class Solution:

    def shortestPath(self, adj_list, source, destination):

        n = len(adj_list)

        # Shortest distance from source
        dist = [float('inf')] * n
        dist[source] = 0

        # parent[i] tells us from which node we reached i
        parent = [i for i in range(n)]

        # (distance, node)
        q = []
        heapq.heappush(q, (0, source))

        while q:

            node_dist, node = heapq.heappop(q)

            # Ignore stale heap entries
            if node_dist > dist[node]:
                continue

            # Early stopping
            if node == destination:
                break

            for neighbor, weight in adj_list[node]:

                new_dist = node_dist + weight

                if new_dist < dist[neighbor]:

                    # Update shortest distance
                    dist[neighbor] = new_dist

                    # Store predecessor
                    parent[neighbor] = node

                    # Push updated distance
                    heapq.heappush(q, (new_dist, neighbor))

        # Destination is unreachable
        if dist[destination] == float('inf'):
            return []

        # Reconstruct path
        path = []
        node = destination

        while parent[node] != node:
            path.append(node)
            node = parent[node]

        # Add source
        path.append(source)

        # We collected destination -> source
        path.reverse()

        return path
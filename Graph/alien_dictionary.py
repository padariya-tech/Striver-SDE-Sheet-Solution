from collections import deque


class Solution:

    def make_adj_list(self, graph, unique_char):

        # Map character -> number
        char_to_num = {}

        for i, ch in enumerate(unique_char):
            char_to_num[ch] = i

        # Create numeric adjacency list
        adj_list = [[] for _ in range(len(unique_char))]

        for edge in graph:
            u = char_to_num[edge[0]]
            v = char_to_num[edge[1]]

            adj_list[u].append(v)

        return adj_list, char_to_num

    def compare_words(self, w1, w2, unique_char):

        n = len(w1)
        m = len(w2)

        i, j = 0, 0
        ans = []

        while i < n and j < m:

            # Add every character
            unique_char.add(w1[i])
            unique_char.add(w2[j])

            # First different character gives the ordering
            if w1[i] != w2[j]:

                ans.append(w1[i])
                ans.append(w2[j])

                break

            i += 1
            j += 1

        # Add remaining characters
        while i < n:
            unique_char.add(w1[i])
            i += 1

        while j < m:
            unique_char.add(w2[j])
            j += 1

        return ans

    def findOrder(self, words: list[str]) -> str:

        n = len(words)

        graph = []
        unique_char = set()

        # Build character graph
        i = 1

        while i < n:

            w1 = words[i - 1]
            w2 = words[i]

            relation = self.compare_words(
                w1,
                w2,
                unique_char
            )

            if relation:
                graph.append(relation)

            i += 1

        # Convert character graph to numeric adjacency list
        adj_list, char_to_num = self.make_adj_list(
            graph,
            unique_char
        )

        print("Character graph:", graph)
        print("Character -> Number:", char_to_num)
        print("Numeric adjacency list:", adj_list)

        # -------------------------
        # Topological Sort (Kahn)
        # -------------------------

        n = len(unique_char)

        # Calculate indegree
        indegree = [0] * n

        for node in range(n):
            for neighbor in adj_list[node]:
                indegree[neighbor] += 1

        # Add nodes with 0 indegree
        q = deque()

        for i in range(n):
            if indegree[i] == 0:
                q.append(i)

        topo_order = []

        while q:

            node = q.popleft()

            topo_order.append(node)

            for neighbor in adj_list[node]:

                indegree[neighbor] -= 1

                if indegree[neighbor] == 0:
                    q.append(neighbor)

        # Cycle exists
        if len(topo_order) != n:
            return ""

        # Number -> Character
        num_to_char = {}

        for ch, num in char_to_num.items():
            num_to_char[num] = ch

        # Convert topological order back to characters
        answer = ""

        for node in topo_order:
            answer += num_to_char[node]

        return answer


if __name__ == "__main__":

    words = ["baa", "abcd", "abca", "cab", "cad"]

    sol = Solution()

    answer = sol.findOrder(words)

    print("Answer:", answer)
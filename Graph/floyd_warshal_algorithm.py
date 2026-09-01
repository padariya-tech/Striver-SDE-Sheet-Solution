# multisource shortest path algorithm
# I want to find the shortest paths for the whole matrix by trying each vertex k as an intermediate."
class Solution:
    def shortest_distance(self, matrix):
        n = len(matrix)

        # Step 1: Convert -1 to infinity
        # and set diagonal elements to 0
        for i in range(n):
            for j in range(n):

                if matrix[i][j] == -1:
                    matrix[i][j] = 10**9

                if i == j:
                    matrix[i][j] = 0

        # Step 2: Floyd-Warshall Algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):

                    matrix[i][j] = min(
                        matrix[i][j],
                        matrix[i][k] + matrix[k][j]
                    )

        # Step 3: Convert infinity back to -1
        for i in range(n):
            for j in range(n):

                if matrix[i][j] == 10**9:
                    matrix[i][j] = -1


if __name__ == "__main__":

    matrix = [
        [0, 5, -1, 10],
        [-1, 0, 3, -1],
        [-1, -1, 0, 1],
        [-1, -1, -1, 0]
    ]

    sol = Solution()

    sol.shortest_distance(matrix)

    for row in matrix:
        print(row)
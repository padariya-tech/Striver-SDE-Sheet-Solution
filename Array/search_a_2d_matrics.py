from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        lo = 0
        hi = m * n - 1

        while lo <= hi:

            mid = (lo + hi) // 2
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                hi = mid - 1
            else:
                lo = mid + 1

        return False
        

if __name__ == "__main__":
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    search_matrix = Solution()
    target = 13
    answer = search_matrix.searchMatrix(matrix,target)
    print(answer)
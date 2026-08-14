import heapq
class Median:

    # solution:- 1 === >  using priority queue (minheap)

    # def median(self,mat):

    #     # Explanation:
    #     # we want sorted order's median and that we can get by storing in min heap such a way that 
    #     # each pop will give the min element and for that we will insert the first of all the rows 
    #     # and then pop the min from it and insert the next element from that row only 
    #     rows = len(mat)
    #     cols = len(mat[0])

    #     minHeap = [] # maximum size is number of rows
    #     medianIndex = (rows * cols) // 2
    #     count = 0
    #     result = -1

    #     # add the first element of each rows
    #     for i in range(rows):
    #         heapq.heappush(minHeap,[mat[i][0],i,0])  # rows * log(rows)

    #     # print(minHeap)
    #     while count <= medianIndex:  # O((rows * cols) // 2 * log(rows))
    #         val,row,col = heapq.heappop(minHeap)  # log(rows)

    #         result = val
    #         # print(val)
    #         count += 1

    #         if col + 1 < cols:
    #             heapq.heappush(minHeap,[mat[row][col+1],row,col+1])  # log(rows)

    #     return result
    #     # total time complexity = O( rows * cols * log(rows) )
    #     # space complexity = O(rows)

    # using binary search
    def count_right_bicection(self,col,val): # o(log(len(col))))
        n = len(col)

        low = 0
        high =  n - 1 
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if col[mid] > val:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans
    def median(self, mat):
        rows = len(mat)
        cols = len(mat[0])

        min_element = float('inf')
        max_element = float('-inf')

        for i in range(rows):  # tc = O(rows)
            min_element = min(min_element, mat[i][0])
            max_element = max(max_element, mat[i][cols - 1])

        # print(min_element, max_element,0,0)
        low = min_element
        high = max_element
        # answer = 0
        k = (rows * cols + 1) // 2
        # median = median - 1
        # first value where count(<= x) >= k is the median.
        while low <= high:  # tc = O(log(max_element - min_element) * rows * log(cols))
            mid = (low + high) // 2
            # print(low, high, mid)
            count = 0
            for i in range(rows):
                count += self.count_right_bicection(mat[i], mid)
                
            # print(count , mid)
            # [ number of elements <= mid ] >= median
            # first value satisfying a condition
            if count < k:
                # answer = mid
                low = mid + 1
            else:
                answer = mid
                high = mid - 1

        return answer


if __name__ == "__main__":
    mat = [
        [1,3,5],
        [2,6,9],
        [3,6,9]
    ]
    find_median = Median()
    ans = find_median.median(mat)
    print(ans)
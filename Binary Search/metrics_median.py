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

        while low <= high:
            mid = (low + high) // 2
            if col[mid] <= val:
                low = mid + 1
            else:
                high = mid - 1

        return low
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

        median = (rows * cols + 1) // 2
        # median = median - 1
        while low <= high:  # tc = O(log(max_element - min_element) * rows * log(cols))
            mid = (low + high) // 2
            # print(low, high, mid)
            count = 0
            for i in range(rows):
                count += self.count_right_bicection(mat[i], mid)
                
            # print(count , mid)
            if count < median:
                low = mid + 1
            else:
                high = mid - 1

        return low


if __name__ == "__main__":
    mat = [
        [1,1,1],
        [2,2,2],
        [3,3,3],
        [1,2,3],
        [4,5,6]
    ]
    find_median = Median()
    ans = find_median.median(mat)
    print(ans)
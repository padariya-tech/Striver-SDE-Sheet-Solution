class Solution:

    def find_student(self,arr,mid):
        result = 1
        summ = 0

        for i in range(len(arr)):
            if summ + arr[i] <= mid:
                summ += arr[i]
            else:
                summ = arr[i]
                result += 1
        # print(result)
        return result

    def findPages(self,arr,k):

        n = len(arr)
        lo = max(arr)
        hi = sum(arr)
        # print(lo,hi)
        answer = 0
        if k > n:
            return -1
        while lo <= hi:
            mid = (lo + hi) // 2
            # print(mid)
            possible_k = self.find_student(arr,mid)

            if possible_k <= k:
                answer = mid
                hi = mid - 1
            else:
                lo = mid + 1

        return answer 

if __name__=="__main__":

    arr= [12,34,67,90]
    k = 2
    pages = Solution()

    answer = pages.findPages(arr,k)

    print(answer)
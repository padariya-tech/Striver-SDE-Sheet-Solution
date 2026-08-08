class Solution:
    def foundCows(self,arr,mid):
        n = len(arr)

        result = 1
        c1 = 0
        for i in range(1,n):
            if arr[i] - arr[c1] >= mid:
                result += 1
                c1 = i

        return result

    def aggressiveCows(self, arr, k):
        # code here
        n = len(arr)
        lo = 0
        hi = max(arr) - min(arr)
        arr = sorted(arr)
        print(arr)
        answer = 0
        while lo <= hi:

            mid = (lo + hi) // 2

            possible_cows = self.foundCows(arr,mid)
            print(possible_cows,mid,lo,hi)
            if possible_cows < k:
                
                hi = mid - 1
            else:
                answer = mid
                lo = mid + 1

        return answer


if __name__=="__main__":

    arr= [10,1,2,7,5]
    k = 3
    pages = Solution()

    answer = pages.aggressiveCows(arr,k)

    print(answer)

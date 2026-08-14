class Solution:
    def findMedianSortedArray(self,nums1,nums2,k):
        n = len(nums1)
        m = len(nums2)
        total = n + m
        # half = (total + 1) // 2
        # 0 <= i <= n
        # 0 <= j <= m

        # Then:
        # 0 <= k - i <= m

        # gives:
        # k - m <= i <= k

        # and combining with:
        # 0 <= i <= n

        # we get:
        # max(0, k - m) <= i <= min(k, n)

        # Therefore:

        l = max(0, k - m)
        r = min(k, n)

        while l <= r:

            i = (l + r ) //2 
            j = k - i

            l1 = float('-inf') if i == 0 else nums1[i-1]
            r1 = float('inf') if i == n else nums1[i]
            l2 = float('-inf') if j == 0 else nums2[j-1]
            r2 = float('inf') if j == m else nums2[j]

            if l1 <= r2 and l2 <= r1:
                return float(max(l1,l2))
                
            if l1 > r2:
                r  = i - 1
            else:
                l = i + 1
        




if __name__ == "__main__":
    median = Solution()
    nums1=[1, 4, 8, 10, 12]
    nums2=[5, 7, 11, 15, 17]
    k = 6
    if len(nums1) > len(nums2):
        nums1,nums2 = nums2,nums1
    answer = median.findMedianSortedArray(nums1,nums2,k)
    print(answer)
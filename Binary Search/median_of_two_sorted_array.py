class Solution:
    def findMedianSortedArray(self,nums1,nums2):
        n = len(nums1)
        m = len(nums2)
        total = n + m
        half = (total + 1) // 2

        l = 0
        r = n

        while l <= r:

            i = (l + r ) //2 
            j = half - i

            l1 = float('-inf') if i == 0 else nums1[i-1]
            r1 = float('inf') if i == n else nums1[i]
            l2 = float('-inf') if j == 0 else nums2[j-1]
            r2 = float('inf') if j == m else nums2[j]

            if l1 <= r2 and l2 <= r1:
                if total % 2 == 1:
                    return float(max(l1,l2))
                else:
                    return (max(l1,l2) + min(r1,r2))/2.0
                
            if l1 > r2:
                r  = i - 1
            else:
                l = i + 1
        




if __name__ == "__main__":
    median = Solution()
    nums1=[1,7,8,9,10]
    nums2=[2,4,6]
    if len(nums1) > len(nums2):
        nums1,nums2 = nums2,nums1
    answer = median.findMedianSortedArray(nums1,nums2)
    print(answer)
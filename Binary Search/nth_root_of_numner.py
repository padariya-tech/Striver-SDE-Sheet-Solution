class Solution:
    def calculate_power(self,mid,n,m):
        result = 1
        for _ in range(n):
            result *= mid
            
            if result > m:
                return result
        return result
    def nthRoot(self, n, m):
       # code here
        if m == 0:
           return 0
        if n == 1:
            return m
            
        left = 0
        right = m
        
        while left <= right:
            mid = (left + right) // 2
            power = self.calculate_power(mid,n,m)
            if power == m:
                return mid
            elif power > m:
                right = mid - 1
            else:
                left = mid + 1
                
        
        return -1

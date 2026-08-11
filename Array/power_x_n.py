from typing import List
class Solution:
    def myPow(self, x:float,n:int) -> float:
        ans = 1
        while n > 0:
            if n % 2 == 0:
                x = x * x
                n = n / 2
                print("from n mod 2 == 0")
                print(x,n)
            else:
                n = n - 1
                ans = x * ans
                print("from n mod == 1")
                print(x,n,ans)
        return ans
        
if __name__ == "__main__":

    sol = Solution()
    x=2.00000
    n = 10
    answer = sol.myPow(x,n)
    print(answer)